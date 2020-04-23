import mysignals as sigs
from matplotlib import pyplot
from matplotlib import style
from scipy.fftpack import fft, ifft
import numpy as np 

freq_domain_signal = fft(sigs.ecg_signal)
time_domain_signal = ifft(freq_domain_signal)

magnitude = np.abs(freq_domain_signal)

style.use("ggplot")

main, plt_arr = pyplot.subplots(4, sharex=True)
main.suptitle("Fast Fourier Transform(FFT)")

plt_arr[0].plot(sigs.ecg_signal)
plt_arr[0].set_title("Time domain input signal")

plt_arr[1].plot(freq_domain_signal)
plt_arr[1].set_title("Frequency domain (FFT) input signal")

plt_arr[2].plot(magnitude)
plt_arr[2].set_title("Magnitue")

plt_arr[3].plot(time_domain_signal)
plt_arr[3].set_title("Time Domain (IFFT)")


pyplot.show()