from scipy import signal
import numpy as np 
from matplotlib import pyplot as plt 

# filter  with passband 0.2-0.4hz, stopband 0-0.1Hz and 0.45-0.5Hz
# remez exchange algorithm

bpass = signal.remez(72, [0, 0.1, 0.2, 0.4, 0.45, 0.5], [0, 1, 0])
freq, response = signal.freqz(bpass)
amplitude = abs(response)

plt.semilogy(freq/(2*np.pi), amplitude, 'g-')
plt.grid()
plt.show()


