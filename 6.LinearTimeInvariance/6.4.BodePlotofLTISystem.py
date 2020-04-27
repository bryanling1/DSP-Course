from scipy import signal
from matplotlib import pyplot as plt 
import numpy as np 

#transfer function H(s) = s^2/s^2+s

s1 = signal.lti([1], [1, 1])
w, mag, phase = s1.bode()

plt.figure()
plt.semilogx(w, mag)
plt.figure()
plt.semilogx(w, phase)
plt.show()