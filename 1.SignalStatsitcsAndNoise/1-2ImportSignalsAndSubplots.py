from matplotlib import pyplot
from matplotlib import style
import mysignals as sig

style.use("ggplot")
style.use("dark_background")
f,pltr_arr = pyplot.subplots(3, sharex = True)
f.suptitle("Multiplot")


pltr_arr[0].plot(sig.InputSignal_1kHz_15kHz, color="magenta")
pltr_arr[0].set_title("Subplot 1", color="magenta")
pltr_arr[1].plot(sig.InputSignal_1kHz_15kHz)
pltr_arr[2].plot(sig.InputSignal_1kHz_15kHz)
pyplot.show()


