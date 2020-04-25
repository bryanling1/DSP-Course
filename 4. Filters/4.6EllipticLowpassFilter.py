from scipy import signal
from matplotlib import pyplot as plt
import numpy as np

b,a = signal.ellip(4, 5, 40, 100, 'low', analog=True)

w,h = signal.freqs(b, a)

plt.xscale("log")
plt.plot(w, 20*np.log10(abs(h)))
plt.title("Elliptic filter frequency response(rp=5, rs=40)")
plt.xlabel("Frequency (rads/second)")
plt.ylabel("Amplitude (db)")
plt.margins(0, 0.1)
plt.grid(which="both", axis="both")

plt.axvline(100, color="magenta")
plt.axhline(-40, color="red")
plt.axhline(-5, color="green")

plt.show()
