# TO ADD TO DB USE THIS
from backend.upload.process_spotify import process_spotify_url
from backend.upload.youtube_download import download_audio_from_youtube
from backend.upload.store_pipeline import store_song_and_fingerprint
# add urls to be added to db here
spotify_urls = [] 

for url in spotify_urls:
    try:
        metadata, query = process_spotify_url(url)
        audio_path, video_id = download_audio_from_youtube(query, metadata["id"])
        metadata["youtube_video_id"] = video_id
        store_song_and_fingerprint(metadata, audio_path)
        print(f"✅ Added: {metadata['title']} by {metadata['artist']}")
    except Exception as e:
        print(f"❌ Failed to add from {url}: {e}")
        
        
# TO TEST USE THIS
# from backend.recognition.match_snippet import match_snippet

# results = match_snippet("your_snippet.wav")
# for song, score in results:
#     print(f"🎯 Match: {song.title} by {song.artist} (score = {score})")
