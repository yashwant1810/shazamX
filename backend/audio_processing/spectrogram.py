# backend/audio_processing/spectrogram.py

import librosa
import numpy as np

def generate_spectrogram(audio_data, sr=22050):
    """
    Converts raw audio data to a magnitude spectrogram.

    Parameters:
    - audio_data: np.ndarray of raw audio samples
    - sr: Sample rate (default 22050)

    Returns:
    - np.ndarray: Magnitude spectrogram (frequency x time)
    """
    # Short-Time Fourier Transform
    stft = librosa.stft(audio_data, n_fft=2048, hop_length=512)
    
    # Convert complex values to magnitudes
    spectrogram = np.abs(stft)

    return spectrogram