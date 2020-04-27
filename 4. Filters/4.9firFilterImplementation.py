from scipy import signal
from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np

sampling_rate = 100
nsamples = 400

t = np.arange(nsamples) / sampling_rate

x1 = np.cos(2*np.pi*0.5*t) + 0.2*np.sin(2*np.pi * 2.5*t*0.1)
x2 = 0.2*np.sin(2*np.pi*15.3) + 0.1*np.sin(2*np.pi*16.7*t+0.1)
x3 = 0.1*np.sin(2*np.pi*23,45*t*0.8)

x = x1+x2+x3

#create FIR filter
nyq_rate = sampling_rate/2.0
width = 5.0/nyq_rate
ripple_db = 60.0

N, beta = signal.kaiserord(ripple_db, width)
fc_hz = 10.0

taps = signal.firwin(N, fc_hz/nyq_rate, window=("kaiser", beta))

fitlered_x = signal.lfilter(taps, 1.0, x)

plt.figure(1)
plt.plot(taps, "bo-", linewidth=2)
plt.title("Filter Coefficients (%d taps)" %N)

plt.figure(2)

w, h = signal.freqz(taps, worN=8000)
plt.plot((w/np.pi)*nyq_rate, abs(h), linewidth=2, color="blue")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Gain")
plt.ylim(-0.05, 1.05)
plt.grid()

#upper inset plot
ax1 = plt.axes([0.42, 0.6, 0.45, 0.25])
plt.plot((w/np.pi)*nyq_rate, abs(h), linewidth=2, color="red")
plt.xlim(0, 8.0)
plt.ylim(0.9985, 1.001)
plt.grid()

#lower inset plot
ax2 = plt.axes([0.42, 0.25, 0.45, 0.25])
plt.plot((w/np.pi)*nyq_rate, abs(h), linewidth=2, color="red")
plt.xlim(12.0, 20.0)
plt.ylim(0.0, 0.0025)
plt.grid()

plt.show()
