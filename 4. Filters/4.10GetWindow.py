from scipy import signal
from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np

triangle_window = signal.get_window('triang', 30)
kaiser_window = signal.get_window(("kaiser", 4.0), 30)
kaiser_window2 = signal.get_window(4.0, 30)
hamm_window = signal.get_window("hamming", 30)
black_window = signal.get_window("blackman", 30)

main, plt_arr = plt.subplots(4, sharex=True)
main.suptitle("Windows")
 
plt_arr[0].plot(triangle_window)
plt_arr[0].set_title("Triangular Window")

plt_arr[1].plot(kaiser_window)
plt_arr[1].set_title("Kaiser Window")

plt_arr[2].plot(hamm_window)
plt_arr[2].set_title("Hamming Window")

plt_arr[3].plot(black_window)
plt_arr[3].set_title("Blackman Window")

plt.show()