pip install numpy scipy

import numpy as np
from scipy import signal
from scipy.fft import fft

# Sample RR intervals in milliseconds
rr_intervals = np.array([800, 810, 780, 790, 820, 800, 830, 810])

# Convert RR intervals from milliseconds to seconds
rr_intervals_seconds = rr_intervals / 1000.0

# Calculate RMSSD
diff_rr_intervals = np.diff(rr_intervals_seconds)
squared_diff_rr_intervals = diff_rr_intervals ** 2
rmssd = np.sqrt(np.mean(squared_diff_rr_intervals))

# Calculate SDNN
sdnn = np.std(rr_intervals_seconds, ddof=1)

# Frequency Domain Analysis for LF/HF Ratio
def calculate_lf_hf(rr_intervals):
    # Interpolate RR intervals to get evenly spaced samples
    timestamp = np.cumsum(rr_intervals_seconds) - rr_intervals_seconds[0]
    interpolated_rr = np.interp(np.arange(timestamp[0], timestamp[-1], 1/4), timestamp, rr_intervals_seconds)  # 4 Hz sampling rate
    
    # Remove DC component and taper signal
    interpolated_rr_detrended = signal.detrend(interpolated_rr)
    tapered_signal = interpolated_rr_detrended * np.hanning(len(interpolated_rr_detrended))
    
    # FFT
    fft_result = fft(tapered_signal)
    freq = np.fft.fftfreq(len(tapered_signal), 1/4)
    
    # Calculate power spectral density
    psd = np.abs(fft_result) ** 2
    lf = np.trapz(psd[(freq >= 0.04) & (freq <= 0.15)])
    hf = np.trapz(psd[(freq >= 0.15) & (freq <= 0.4)])
    
    return lf / hf

lf_hf_ratio = calculate_lf_hf(rr_intervals_seconds)

print(f"RMSSD: {rmssd:.2f} s")
print(f"SDNN: {sdnn:.2f} s")
print(f"LF/HF Ratio: {lf_hf_ratio:.2f}")
