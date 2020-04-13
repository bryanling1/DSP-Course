from matplotlib import pyplot
from matplotlib import style
import mysignals as sigs
import numpy as np 

output_signal = np.cumsum(sigs.InputSignal_1kHz_15kHz)

#own implementation of running sum algorithm
def calcRunningSum(inp, out):
    for x in range(len(out)):
        out[x] = 0
    
    for x in range(len(inp)):
        out[x] = out[x-1] + inp[x]

calcRunningSum(sigs.InputSignal_1kHz_15kHz, output_signal)

style.use("ggplot")
main, plt_arr = pyplot.subplots(2, sharex=True)
main.suptitle("Running Sum")

plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz)
plt_arr[0].set_title("Input signal")

plt_arr[1].plot(output_signal)
plt_arr[1].set_title("Output signal")

pyplot.show()

#this shows the running sum can be used to find peaks in signals (simplify)