import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = r"C:\Users\Saravanan\Downloads\signal.csv"
data = pd.read_csv(file)

signal = data['NoisySignal'].values
time = data['Time'].values
sampling_rate = 1 / (time[1] - time[0])
n = len(signal)

fft_signal = np.fft.fft(signal)
freq = np.fft.fftfreq(n, d=1/sampling_rate)
magnitude = np.abs(fft_signal)

threshold = np.max(magnitude) * 0.5  # Keep frequencies with magnitude > 50% of max
# After experimenting different values 50% seemed the best even though it seems high
fft_signal_clean = fft_signal.copy()
fft_signal_clean[magnitude < threshold] = 0

denoised_signal = np.real(np.fft.ifft(fft_signal_clean))

plt.figure(figsize=(15, 10))

plt.subplot(4, 1, 1)
plt.plot(time, signal, 'b-', label='Original Signal', alpha=0.7)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original Signal')
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 2)
positive_freq_mask = freq >= 0
plt.plot(freq[positive_freq_mask], magnitude[positive_freq_mask], 'b-',
         label='Original Frequency Spectrum')
plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Original Frequency Spectrum')
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 3)
magnitude_clean = np.abs(fft_signal_clean)
plt.plot(freq[positive_freq_mask], magnitude_clean[positive_freq_mask], 'r-',
         label='Denoised Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Denoised Frequency Spectrum')
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(time, denoised_signal, 'r-', label='Denoised Signal', linewidth=1.5)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Denoised Signal')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

top_freq_indices = np.argsort(magnitude_clean)[-6:]
print("\nDominant frequencies in the denoised signal:")
for idx in reversed(top_freq_indices):
    if freq[idx] >= 0:
        print(f"Frequency: {freq[idx]:.2f} Hz, Magnitude: {magnitude_clean[idx]:.2f}")