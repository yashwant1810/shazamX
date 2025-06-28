# shazamX — Audio Fingerprinting + Recognition System (Backend)

<img src="https://raw.githubusercontent.com/yashwant1810/shazamX-ui/main/public/BlackSimpleMusicStudioLogo.png" alt="shazamX logo" width="150"/>

## Description

`shazamX` is a Shazam-like audio recognition engine. It fingerprints full-length songs, stores their hashes in a local SQLite database, and matches short audio snippets recorded in the browser. It’s optimized for lightweight setups and runs entirely offline which can also be exposed online using ngrok.

## Key Techniques & Features

- Spectrogram-based fingerprinting using [`librosa.stft`](https://librosa.org/doc/latest/generated/librosa.stft.html)
- Peak pair hashing based on anchor-target models from [Shazam's original paper](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf)
- Custom audio fingerprint comparison using [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
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
- [`ngrok`](https://ngrok.com/docs/getting-started) for exposing server online for hosting purposes

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

This backend is designed to be paired with [`shazamX-ui`](https://github.com/yashwant1810/shazamX-ui). Make sure both are running locally to complete the full audio recognition pipeline.

---

## Exposing the Backend via ngrok

To test your backend from a deployed frontend (like on Vercel), you can expose your local FastAPI server using [ngrok](https://ngrok.com/):

1. Start the backend server:
   ```bash
   uvicorn backend.main:app --host 0.0.0.0 --port 8000
   ```

2. In another terminal, run:
   ```bash
   ngrok http 8000
   ```

3. Use the generated `https://xyz.ngrok-free.app` URL as the `VITE_BACKEND_URL` in your frontend environment variables.

Make sure your FastAPI app has CORS enabled:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

