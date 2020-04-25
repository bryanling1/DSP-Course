from scipy import signal
from matplotlib import pyplot as plt
import numpy as np

b,a = signal.butter(4, 100, "low", analog=True)
w,h = signal.freqs(b, a)

plt.plot(w, 20*np.log10(abs(h)), color="silver", ls="dashed")

b, a = signal.bessel(4, 100, "low", analog=True)
w, h = signal.freqs(b, a)

plt.plot(w, 20*np.log10(abs(h)))
plt.xscale("log")
plt.title("Bessel filter frequency response (with butterworth)")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Amplitude (db)")
plt.margins(0, 0.1)
plt.grid(which="both", axis="both")
plt.axvline(100, color="green")
plt.show()
