import mysignals as sigs
from matplotlib import pyplot
from matplotlib import style
import math

def calc_dft(source_signal):
    N = len(source_signal)
    img_arr = [None] * (N // 2)
    real_arr = [None] * (N // 2)

    #set all value to 0
    for i in range(N // 2):
        img_arr[i] = 0
        real_arr[i] = 0
    
    for i in range(N // 2):
        for j in range(N):
            real_arr[i] += source_signal[j] * math.cos(2*math.pi*i*j/N)
            img_arr[i] -= source_signal[j] * math.sin(2*math.pi*i*j/N)
    
    style.use('ggplot')
    main, plot_arr = pyplot.subplots(3, sharex=True)
    main.suptitle("Discrete Fourier Transform (DFT)")

    plot_arr[0].plot(source_signal)
    plot_arr[0].set_title("Input Signal")

    plot_arr[1].plot(real_arr)
    plot_arr[1].set_title("Real Part")

    plot_arr[2].plot(img_arr)
    plot_arr[2].set_title("Imaginary Part")

    pyplot.show()

calc_dft(sigs.InputSignal_1kHz_15kHz)
