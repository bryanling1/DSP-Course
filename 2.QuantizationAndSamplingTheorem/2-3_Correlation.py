import numpy as np
from scipy import signal 
from matplotlib import pyplot as plt
import mysignals as sigs

corr_output_signal = signal.correlate(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode="same")
conv_output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode="same")

plt.plot(corr_output_signal)
plt.show()

#correlation looks the same as convelution becaus the signal is symmetrical in this case


