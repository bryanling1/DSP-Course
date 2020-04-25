from scipy import signal
from matplotlib import pyplot as plt
import numpy as np

b,a = signal.butter(4, 100, "low", analog=True)
w,h = signal.freqs(b, a)

plt.plot(w, 20*np.log10(abs(h)), color="silver", ls="dashed")
