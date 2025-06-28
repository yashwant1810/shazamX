# TO ADD TO DB USE THIS
from backend.upload.process_spotify import process_spotify_url
from backend.upload.youtube_download import download_audio_from_youtube
from backend.upload.store_pipeline import store_song_and_fingerprint

spotify_urls = ['https://open.spotify.com/track/5ZLtkP7SQXXGrYCX2Uqkqu', 'https://open.spotify.com/track/2jmVM52B5vGc609yAYvh08', 'https://open.spotify.com/track/3qudEWwDUMCZ9HKXrnSFEm', 'https://open.spotify.com/track/19JgM3FZpMMw4KCPjuPm0Z', 'https://open.spotify.com/track/7kU3qKcQXrco0sGAvVtYKu', 'https://open.spotify.com/track/25TjnXucfxMQgtQLVBhGLx', 'https://open.spotify.com/track/7mmC9oJZxmYkIyDeghEGCd', 'https://open.spotify.com/track/4qFUzQvfDAcnmfqQ7gBnid', 'https://open.spotify.com/track/7vvmU5ayTrVWiNVxiwHLQI', 'https://open.spotify.com/track/1xEDyLLmFKjt66xtqq0d3w', 'https://open.spotify.com/track/35tYFzDgLwSTcyaX56ZXyl', 'https://open.spotify.com/track/6hjyO0dIJHAeJsQPxogh37', 'https://open.spotify.com/track/3vC8i2pXwxJUpnOmXXkb6i', 'https://open.spotify.com/track/493Gva5Q50Bo5nqj7rfKex', 'https://open.spotify.com/track/28h5xXPVfkUTRfMw4S0lwV', 'https://open.spotify.com/track/6UPH8T6KYQUWmH2521KkKQ', 'https://open.spotify.com/track/37ZFkN5esLp0gSmidfIS2T', 'https://open.spotify.com/track/2HLi2O9Y5qpBOjZ23A0mvu', 'https://open.spotify.com/track/03gyypnQJAVHQvvvMDzBry', 'https://open.spotify.com/track/0WCtgV9JCrrFrLAB6qRu9g', 'https://open.spotify.com/track/1kHc3qvETQWKvBMCIkcoPQ', 'https://open.spotify.com/track/1alInstEk6TQMuPyjCgI4K', 'https://open.spotify.com/track/6btegcu44HqquqArljhFxu', 'https://open.spotify.com/track/4q7ls1XOMHmZCvTYAqNhxZ', 'https://open.spotify.com/track/1Jsos1mzwTwYGOndYN5h8V', 'https://open.spotify.com/track/1u3KTMxSOXMX0cbb5BKGdc', 'https://open.spotify.com/track/4EPeNXrBhpUPQ6gtSCQV4R', 'https://open.spotify.com/track/55rsHTpDenL0DajypexEI6', 'https://open.spotify.com/track/2ImHVd8DsAZkvfLRbis8wU', 'https://open.spotify.com/track/2dPW1RLeV4beremRtbAsAm', 'https://open.spotify.com/track/6H6yFqMZoJfutYdmeiG5Bz', 'https://open.spotify.com/track/5RtgfvKnnHyGXuUwFy3ePw', 'https://open.spotify.com/track/0ZsPjTNRzXm0qyT5fSLa3g', 'https://open.spotify.com/track/0XUrsVswMdWhOXWMMZLTy5', 'https://open.spotify.com/track/5nPbBpS7oaX1Y9P8vmIa8b', 'https://open.spotify.com/track/5XseQZ9TGr06Rv1Ye6wCu0']


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