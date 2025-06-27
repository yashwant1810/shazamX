# tests/test_spectrogram.py

import sys
import os

# Add the backend directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

import librosa
from audio_processing.spectrogram import generate_spectrogram

def test_generate_spectrogram():
    # Load example audio
    audio, sr = librosa.load(librosa.example('trumpet'), sr=22050)
    spectrogram = generate_spectrogram(audio, sr)

    assert spectrogram.shape[0] > 0
    assert spectrogram.shape[1] > 0
    print("Spectrogram shape:", spectrogram.shape)