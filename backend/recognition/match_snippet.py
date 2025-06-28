import librosa
from collections import defaultdict, Counter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.audio_processing.spectrogram import generate_spectrogram
from backend.audio_processing.peak_extraction import extract_peaks
from backend.audio_processing.fingerprint import generate_fingerprint
from backend.db.models import Fingerprint, Song

def match_snippet(snippet_path: str, db_path="sqlite:///shazam.db", top_k=1):
    """
    Match a short audio snippet against the fingerprint DB.

    Args:
        snippet_path (str): Path to a .wav snippet
        db_path (str): Path to SQLite database

    Returns:
        List of (song, score) tuples
    """
    # Load snippet audio
    audio, sr = librosa.load(snippet_path, sr=22050)
    spectrogram = generate_spectrogram(audio, sr)
    peaks = extract_peaks(spectrogram, sr)
    snippet_fps = generate_fingerprint(peaks)

    # DB setup
    engine = create_engine(db_path)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Match: hash → (db_time - snippet_time) per song
    offset_counts = defaultdict(Counter)

    for hash_val, entries in snippet_fps.items():
        db_matches = session.query(Fingerprint).filter(Fingerprint.hash == hash_val).all()

        for match in db_matches:
            for snippet_time, _ in entries:
                offset = match.timestamp - snippet_time
                offset_counts[match.song_id][round(offset, 1)] += 1

    # Score: for each song, get best offset hit count
    song_scores = []
    for song_id, offsets in offset_counts.items():
        best_offset = offsets.most_common(1)[0]
        total_matches = best_offset[1]
        song = session.query(Song).get(song_id)
        song_scores.append((song, total_matches))

    song_scores.sort(key=lambda x: x[1], reverse=True)

    if song_scores:
        song, score = song_scores[0]
        result = {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "album": song.album,
            "duration": song.duration,
            "spotify_url": song.spotify_url,
            "youtube_video_id": song.youtube_video_id,
            "created_at": str(song.created_at),
            "score": score
        }
    else:
        result = "No match found"

    session.close()
    return result