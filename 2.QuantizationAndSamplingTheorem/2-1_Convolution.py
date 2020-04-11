from matplotlib import pyplot
from matplotlib import style
import mysignals as sigs
from scipy import signal

# output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode='same') 

# Design our own convolution algorithm
def convolution(sig_src_arr, imp_response_arr):
    sig_dest_array = [0] * (len(sig_src_arr) + len(imp_response_arr))
    for x in range(len(sig_src_arr) + len(imp_response_arr)):
        sig_dest_array[x] = 0
    
    for x in range(len(sig_src_arr)):
        for y in range(len(imp_response_arr)):
            sig_dest_array[x+y] += sig_src_arr[x] * imp_response_arr[y]

    return sig_dest_array

output_signal = convolution(sigs.Impulse_response, sigs.InputSignal_1kHz_15kHz)

style.use("ggplot")

main, plot_array = pyplot.subplots(3, sharex=True)
main.suptitle("Convolution")
plot_array[0].plot(sigs.InputSignal_1kHz_15kHz)
plot_array[0].set_title("Input Signal")
#low pass frequency of 6khz
plot_array[1].plot(sigs.Impulse_response)
plot_array[1].set_title("Impulse Response")
plot_array[2].plot(output_signal)
plot_array[2].set_title("Output Signal")

pyplot.show()