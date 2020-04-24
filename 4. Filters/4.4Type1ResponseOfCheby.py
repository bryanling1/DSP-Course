from scipy.signal import freqs, iirfilter
from matplotlib import pyplot as plt
import numpy as np

b, a = iirfilter(4, [1, 10], 1, 60, analog=True, ftype="cheby1")

w, h = freqs(b, a, worN=np.logspace(-1, 2, 1000))

plt.semilogx(w, np.abs(h))
plt.xlabel("Frequency")
plt.ylabel("Amplitude Response")
plt.grid()
plt.show()