import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

import librosa
from audio_processing.spectrogram import generate_spectrogram
from audio_processing.peak_extraction import extract_peaks
from audio_processing.fingerprint import generate_fingerprint

from audio_processing.fingerprint import generate_fingerprint

def test_generate_fingerprint():
    # Load example audio
    audio, sr = librosa.load(librosa.example('trumpet'), sr=22050)
    spectrogram = generate_spectrogram(audio, sr)
    peaks = extract_peaks(spectrogram, sr)
    fingerprint = generate_fingerprint(peaks, song_id='test_song')

    assert isinstance(fingerprint, dict)
    assert len(fingerprint) > 0
    sample_hash = next(iter(fingerprint))
    assert isinstance(sample_hash, int)
    print("✅ Fingerprint sample:", sample_hash, "->", fingerprint[sample_hash][:3])