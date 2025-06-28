import librosa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.db.models import Song, Fingerprint
from backend.audio_processing.spectrogram import generate_spectrogram
from backend.audio_processing.peak_extraction import extract_peaks
from backend.audio_processing.fingerprint import generate_fingerprint

def store_song_and_fingerprint(metadata: dict, audio_path: str, db_path="sqlite:///shazam.db"):
    """
    Run fingerprinting on the downloaded audio and store in the database.

    Args:
        metadata (dict): Song metadata (id, title, artist, album, duration, spotify_url)
        audio_path (str): Path to downloaded .wav audio file
        db_path (str): SQLite DB path
    """
    # Load audio and generate fingerprints
    audio_data, sr = librosa.load(audio_path, sr=22050)
    spectrogram = generate_spectrogram(audio_data, sr)
    peaks = extract_peaks(spectrogram, sr)
    fingerprint_dict = generate_fingerprint(peaks, song_id=metadata["id"])

    # DB setup
    engine = create_engine(db_path)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert song metadata
    song = Song(
        id=metadata["id"],
        title=metadata["title"],
        artist=metadata["artist"],
        album=metadata["album"],
        duration=metadata["duration"],
        spotify_url=metadata["spotify_url"],
        youtube_video_id=metadata.get("youtube_video_id"),
        created_at="NOW()"  # You can replace with datetime.utcnow().isoformat()
    )
    session.add(song)

    # Insert fingerprints
    for hash_val, entries in fingerprint_dict.items():
        for timestamp, _ in entries:
            session.add(Fingerprint(hash=hash_val, timestamp=timestamp, song_id=song.id))

    session.commit()
    session.close()
    print(f"✅ Stored {len(fingerprint_dict)} hashes for '{metadata['title']}'")