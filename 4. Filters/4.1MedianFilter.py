from matplotlib import pyplot
from matplotlib import style
import mysignals as sigs
from scipy import signal

style.use("ggplot")

median_filter_output = signal.medfilt(sigs.InputSignal_1kHz_15kHz, 11)

main, plot_arr = pyplot.subplots(2, sharex=True)
main.suptitle="Median Filter"

plot_arr[0].plot(sigs.InputSignal_1kHz_15kHz)
plot_arr[0].set_title("input signal")

plot_arr[1].plot(median_filter_output)
plot_arr[1].set_title("median filter")
pyplot.show()