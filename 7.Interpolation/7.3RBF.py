from scipy import interpolate
from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np 

x = np.linspace(0, 10, 9)
y = np.sin(x)

xi = np.linspace(0, 10, 101)
spline = interpolate.UnivariateSpline(x, y)
yspline = spline(xi)

Uspline = interpolate.InterpolatedUnivariateSpline(x, y)
yUspline = Uspline(xi)

rbf = interpolate.Rbf(x, y)
y_rbf = rbf(xi)
plt.plot(x, y, "bo")
plt.plot(xi, yspline, "b")
plt.plot(xi, yUspline, "g")
plt.plot(xi, y_rbf, "r")
plt.legend(["plot", "Univariated", "Univariated interpolated" ,"with RBF"])

plt.show()