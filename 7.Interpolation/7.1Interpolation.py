from scipy import interpolate
from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np 

x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)

f1 = interpolate.interp1d(x, y, kind="linear")
f2 = interpolate.interp1d(x, y, kind="cubic")

x_new = np.linspace(0, 4, 30)
plt.plot(x, y, "go", x_new, f1(x_new),"r", x_new, f2(x_new), "b")
plt.legend(["data", "linear", "cubic"])
plt.grid()

plt.show()