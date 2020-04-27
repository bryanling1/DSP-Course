from scipy import signal
from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np
from scipy.fftpack import fft, fftshift

t = np.linspace(0, 1, 2001)

sig_5hz = np.sin(2*np.pi*5*t)
sig_250hz = np.sin(2*np.pi*250*t)
sig_5hz_250hz = sig_5hz + sig_250hz

#cutoff frequenct of 125, normalize by multilying by 8 
b, a = signal.butter(8,0.125)
#padlen: padd first to zeros
filtered_signal = signal.filtfilt(b, a, sig_5hz_250hz, padlen=150)


main, plt_arr = plt.subplots(4, sharex=True)

plt_arr[0].plot(sig_5hz)
plt_arr[0].set_title("5 Hz")

plt_arr[1].plot(sig_250hz)
plt_arr[1].set_title("250 Hz")

plt_arr[2].plot(sig_5hz_250hz)
plt_arr[2].set_title("Combined Signal")

plt_arr[3].plot(filtered_signal)
plt_arr[3].set_title("Filtered Signal")

plt.show()


