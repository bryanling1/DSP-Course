from scipy import signal
from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np 

original_signal = np.repeat([0,1,1,0,1,0,0,1], 128)
noise = np.random.randn(len(original_signal))
noise_signal = original_signal + noise
rectangular_pulse = np.ones(128)

#used to identify certain features of the signal
correlated_output = signal.correlate(noise_signal, rectangular_pulse, mode="same")

clock = np.arange(64, len(original_signal), 128)

main, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1, sharex=True)

ax_orig.plot(original_signal)
ax_orig.plot(clock, original_signal[clock], 'ro')

ax_noise.plot(noise_signal)

ax_corr.plot(correlated_output)
ax_corr.plot(clock, correlated_output[clock], 'ro')

ax_orig.margins(0,0.1)
main.tight_layout()
plt.show()
