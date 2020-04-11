from matplotlib import pyplot
from matplotlib import style
import mysignals as sig

style.use("ggplot")
main, plot_array = pyplot.subplots(2, sharex = True)
main.suptitle("Input signal and impulse response")

plot_array[0].plot(sig.InputSignal_1kHz_15kHz)
plot_array[1].plot(sig.Impulse_response)

pyplot.show()
