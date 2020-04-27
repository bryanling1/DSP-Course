import numpy as np 
from scipy import signal
from matplotlib import pyplot as plt 

#generate a noisy signal to be filtered
t = np.linspace(-1, 1, 201)

x1 = np.sin(2*np.pi*0.75*t*(1-t))
x2 = 2.1 + 0.1*np.sin(2*np.pi*1.25*t+1)
x3 = 0.18*np.cos(2*np.pi*3.85*t)

x = x1 + x2 + x3
xn = x + np.random.randn(len(t))*0.08

b, a = signal.butter(3, 0.05)

#lfilter twice
zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b,a, xn, zi=zi*xn[0])

z2, _ = signal.lfilter(b, a, z, zi=zi*xn[0])

#filtfilt

y = signal.filtfilt(b, a, xn)


plt.figure(figsize=(10, 5))
plt.plot(t, xn, "b", linewidth = 1.75)
plt.plot(t, z, "r--", linewidth=1.75)
plt.plot(t, z2, "r", linewidth=1.75)
plt.plot(t, y, "g", linewidth=10)

plt.legend(["noise signal", "lfilter_once", "lfilter_twice", "filtfilt"], loc="best")
plt.grid()
plt.show()