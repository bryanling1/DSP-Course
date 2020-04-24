from scipy import signal
from matplotlib import pyplot as plt
import numpy as np

b,a = signal.butter(4, 100, 'low', analog=True)
w,h = signal.freqs(b, a)

plt.plot(w, 20*np.log10(np.abs(h)))
plt.xscale("log")

plt.title('Butterworth filter frequency response')
plt.xlabel("Frequency: rads/seconds")
plt.ylabel("Amplitude: db")
plt.margins(0,0.2)
plt.grid()
plt.axvline(100)
plt.show()
