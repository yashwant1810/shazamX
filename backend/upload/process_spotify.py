# backend/upload/process_spotify.py

from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import os

load_dotenv()  # Load credentials from .env

sp = Spotify(auth_manager=SpotifyClientCredentials())

def process_spotify_url(spotify_url: str):
    """
    Given a Spotify track URL or ID:
    - Fetch metadata from Spotify
    - Build a YouTube search query
    - Return metadata and query string
    """
    try:
        # Get track metadata
        track = sp.track(spotify_url)
        title = track['name']
        artist = track['artists'][0]['name']
        album = track['album']['name']
        duration_ms = track['duration_ms']
        spotify_id = track['id']

        # Build a YouTube search query
        search_query = f"{title} {artist}"

        metadata = {
            "id": spotify_id,
            "title": title,
            "artist": artist,
            "album": album,
            "duration": int(duration_ms / 1000),
            "spotify_url": track['external_urls']['spotify']
        }

        return metadata, search_query

    except Exception as e:
        print("❌ Failed to fetch from Spotify:", e)
        return None, None