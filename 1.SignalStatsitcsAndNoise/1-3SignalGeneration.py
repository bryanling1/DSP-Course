from matplotlib import pyplot
from matplotlib import style
import numpy as np
from scipy import signal

#signal sampling rate 2000Hz
t = np.linspace(0, 1.0, 2001)

sig_5khz = np.sin(2*np.pi*t*5)
sig_100khz = np.sin(2*np.pi*t*100)
add = sig_5khz + sig_100khz

main, pyplot_arr = pyplot.subplots(3, sharex=True)
main.suptitle("Graphs")
pyplot_arr[0].plot(sig_5khz, color="blue")
pyplot_arr[0].set_title("5khz Signal")
pyplot_arr[1].plot(sig_100khz, color="red")
pyplot_arr[1].set_title("100 khz Signal")
pyplot_arr[2].plot(add, color="magenta")
pyplot_arr[2].set_title("5+100khz Signal")

pyplot.show()





