from matplotlib import pyplot
from matplotlib import style
import mysignals as sigs
import numpy as np 

output_signal = np.diff(sigs.InputSignal_1kHz_15kHz)
output_signal = [None] * 320

#own implementation
def calcFirstDifference(input_signal, output_signal):
    for x in range(len(output_signal)): 
        output_signal[x] = 0
    
    for x in range (1, len(input_signal)):
        output_signal[x] = input_signal[x] - input_signal[x-1]

calcFirstDifference(sigs.InputSignal_1kHz_15kHz, output_signal)

style.use("ggplot")
main, plt_arr = pyplot.subplots(2, sharex=True)
main.suptitle("First Difference")

plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz)
plt_arr[0].set_title("Input signal")

plt_arr[1].plot(output_signal)
plt_arr[1].set_title("Output signal")

pyplot.show()

#does not look super useful now, but will later on