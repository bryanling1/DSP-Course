from scipy import signal
from matplotlib import pyplot as plt
import numpy as np

b, a = signal.cheby1(4, 5, 100, 'low', analog=True)
w, h = signal.freqs(b, a)

plt.plot(w, 20*np.log10(abs(h)))
plt.xscale("log")
plt.title("Chebyshex Type 1 freqiemcu response (rp=5)")
plt.xlabel("Frequency: rad/s")
plt.ylabel("Amplitude db")
plt.grid(which='both', axis="both")
plt.axvline(100, color="red")
plt.axhline(-5, color="red")
plt.show()
