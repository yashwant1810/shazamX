

import yt_dlp
import os

def download_audio_from_youtube(search_query: str, track_id: str, output_dir="downloads"):
    """
    Search YouTube for a given query and download the top result as .wav.

    Args:
        search_query (str): The YouTube search query (e.g. "Mr. Brightside The Killers")
        track_id (str): Unique identifier to name the output file (from Spotify)
        output_dir (str): Directory to save downloaded audio

    Returns:
        str: Path to the downloaded .wav file
        str: YouTube video ID
    """
    os.makedirs(output_dir, exist_ok=True)
    output_template = os.path.join(output_dir, f"{track_id}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{search_query}", download=True)
        video = info['entries'][0]
        video_id = video['id']

    audio_path = os.path.join(output_dir, f"{track_id}.wav")
    return audio_path, video_id