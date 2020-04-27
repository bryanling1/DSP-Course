import numpy as np 
from scipy import signal
from matplotlib import pyplot as plt 

t = np.linspace(-10, 10, 10)
y = 1 + t + 0.01*t**2

#constant detrend
yconst = signal.detrend(y, type="constant")
#linear detrend
ylin = signal.detrend(y, type="linear")

plt.plot(t, y, '-rx')
plt.plot(t, yconst, "-bo")
plt.plot(t, ylin, "-k+")
plt.grid()
plt.legend(['signal', "constant.det", "linear.det"])
plt.show()
