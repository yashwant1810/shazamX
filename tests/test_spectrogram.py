# tests/test_spectrogram.py

import sys
import os

# Add the backend directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

import librosa
from audio_processing.spectrogram import generate_spectrogram
from audio_processing.peak_extraction import extract_peaks

def test_generate_spectrogram():
    # Load example audio
    audio, sr = librosa.load(librosa.example('trumpet'), sr=22050)
    spectrogram = generate_spectrogram(audio, sr)

    assert spectrogram.shape[0] > 0
    assert spectrogram.shape[1] > 0
    print("Spectrogram shape:", spectrogram.shape)
    
def test_extract_peaks():
    # Load example audio
    audio, sr = librosa.load(librosa.example('trumpet'), sr=22050)
    spectrogram = generate_spectrogram(audio, sr)
    peaks = extract_peaks(spectrogram, sr)

    assert isinstance(peaks, list)
    assert len(peaks) > 0
    assert all(len(p) == 3 for p in peaks)
    print("✅ Extracted peaks:", peaks[:5])