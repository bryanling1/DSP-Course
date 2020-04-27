from scipy import signal
from matplotlib import pyplot as plt 
import numpy as np 

s1 = signal.lti([], [1, 1, 1], [5])

w, h = signal.freqresp(s1)

#complex plot
plt.plot(h.real, h.imag, "b")
plt.plot(h.real, -h.imag, "r")

plt.show()

