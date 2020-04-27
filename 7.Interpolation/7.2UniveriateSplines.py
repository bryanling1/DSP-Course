from scipy import interpolate
from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np 

x = np.linspace(-3, 3, 50)
y = np.exp(-x**2)+0.1*np.random.randn(50)

plt.plot(x, y, "ro", ms=5)

spline = interpolate.UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)

plt.plot(xs, spline(xs), "g", lw=4)

spline.set_smoothing_factor(0.5)

plt.plot(xs, spline(xs), "b", lw=3)

plt.grid()
plt.show()
