from scipy import signal
from matplotlib import pyplot
import numpy as np 

b = signal.firwin(80, 0.5, window=("kaiser", 8))
pyplot.plot(b)
pyplot.show()
print(b)