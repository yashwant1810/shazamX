import numpy as np

def extract_peaks(spectrogram, sr=22050):
    """
    Identifies prominent frequency peaks in each time slice of the spectrogram.

    Parameters:
    - spectrogram: np.ndarray (frequency x time)
    - sr: sample rate

    Returns:
    - List of (time_idx, freq_idx, magnitude) peaks
    """
    peaks = []
    
    # Define logarithmic frequency bands (6 total)
    freq_bands = [
        (0, 500),      # Low
        (500, 1000),   # Low-mid
        (1000, 2000),  # Mid
        (2000, 3000),  # High-mid
        (3000, 4000),  # High
        (4000, 5000),  # Very high
    ]
    
    n_freq_bins = spectrogram.shape[0]
    time_slices = spectrogram.shape[1]

    # Convert frequency ranges to bin indices
    freq_bin_range = lambda hz: int(hz * n_freq_bins / (sr // 2))

    for time_idx in range(time_slices):
        time_peaks = []

        for low_hz, high_hz in freq_bands:
            low_bin = freq_bin_range(low_hz)
            high_bin = min(freq_bin_range(high_hz), n_freq_bins - 1)

            band_slice = spectrogram[low_bin:high_bin, time_idx]
            if band_slice.size == 0:
                continue

            max_idx = np.argmax(band_slice)
            freq_idx = low_bin + max_idx
            magnitude = band_slice[max_idx]
            time_peaks.append((freq_idx, magnitude))

        # Dynamic threshold: mean magnitude of this time slice
        magnitudes = [mag for _, mag in time_peaks]
        threshold = np.mean(magnitudes)

        for freq_idx, magnitude in time_peaks:
            if magnitude >= threshold:
                peaks.append((time_idx, freq_idx, magnitude))

    return peaks