import hashlib

def generate_fingerprint(peaks, song_id=None):
    """
    Generate fingerprint hashes from peaks.

    Parameters:
    - peaks: List of (time_idx, freq_idx, magnitude)
    - song_id: Optional ID to tag each hash with

    Returns:
    - dict: {hash_value: [(anchor_time, song_id)]}
    """
    fingerprint = {}
    target_zone_width = 10  # time frames to look ahead
    target_zone_height = 100  # frequency range tolerance

    for i, (anchor_time, anchor_freq, _) in enumerate(peaks):
        for j in range(i + 1, min(i + 1 + target_zone_width, len(peaks))):
            target_time, target_freq, _ = peaks[j]

            if abs(target_freq - anchor_freq) > target_zone_height:
                continue

            time_delta = target_time - anchor_time
            if time_delta <= 0:
                continue

            hash_input = f"{anchor_freq}|{target_freq}|{time_delta}"
            hash_bytes = hashlib.md5(hash_input.encode()).digest()
            hash_value = int.from_bytes(hash_bytes[:4], byteorder='big')

            if hash_value not in fingerprint:
                fingerprint[hash_value] = []
            fingerprint[hash_value].append((anchor_time, song_id))

    return fingerprint