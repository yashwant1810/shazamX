# shazamX — Audio Fingerprinting + Recognition System (Backend)

## Description

`shazamX` is a local-first Shazam-like audio recognition engine. It fingerprints full-length songs, stores their hashes in a local SQLite database, and matches short audio snippets recorded in the browser. It’s optimized for lightweight setups and runs entirely offline.

## Key Techniques & Features

- Spectrogram-based fingerprinting using [`librosa.stft`](https://librosa.org/doc/latest/generated/librosa.stft.html)
- Peak pair hashing based on anchor-target models from [Shazam's original paper](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf)
- Custom audio fingerprint comparison using [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- Matching is based on [offset clustering](https://en.wikipedia.org/wiki/Shazam_(service)#Algorithm) to reduce false positives
- Uses `FastAPI` for the minimal `/match` API endpoint
- Metadata sourced using [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- Audio downloaded from YouTube via [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

## Libraries & Tools of Note

- [`librosa`](https://librosa.org/) for signal processing
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for robust YouTube audio scraping
- [`pydub`](https://github.com/jiaaro/pydub) for waveform trimming and exporting
- [`SQLAlchemy`](https://www.sqlalchemy.org/) as the ORM
- [`uvicorn`](https://www.uvicorn.org/) for ASGI server
- [`python-dotenv`](https://github.com/theskumar/python-dotenv) for `.env` loading

## Project Structure

```txt
shazamX/
├── backend/
│   ├── audio_processing/      # Spectrogram and peak extraction functions
│   ├── db/                    # SQLite models and init
│   ├── recognition/           # Fingerprint matching logic
│   ├── upload/                # YouTube + Spotify integration + storage pipeline
│   └── main.py                # FastAPI app for /match endpoint
├── tests/                     # Unit tests for spectrogram, peaks, fingerprints
├── shazam.db                  # Local SQLite DB (ignored by Git)
├── temp.py                    # Manual ingestion script for new songs
```

- `backend/audio_processing/`: Contains spectrogram generation and peak extraction logic.
- `backend/recognition/`: Matching logic for fingerprints.
- `backend/upload/`: Integrates with Spotify and YouTube to collect and process song data.
- `backend/main.py`: Defines the FastAPI app and the `/match` route.
- `temp.py`: Used to ingest Spotify tracks and store them with fingerprints into the local database.

---

This backend is designed to be paired with [`shazamX-ui`](../shazamX-ui). Make sure both are running locally to complete the full audio recognition pipeline.

