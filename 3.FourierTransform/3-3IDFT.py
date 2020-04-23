import mysignals as sigs
from matplotlib import pyplot
from matplotlib import style
import math

def calc_dft(source_signal):
    N = len(source_signal)
    img_arr = [None] * (N // 2)
    real_arr = [None] * (N // 2)
    magn_arr = [None] * (N // 2)

    #set all value to 0
    for i in range(N // 2):
        img_arr[i] = 0
        real_arr[i] = 0
    
    for i in range(N // 2):
        for j in range(N):
            real_arr[i] += source_signal[j] * math.cos(2*math.pi*i*j/N)
            img_arr[i] -= source_signal[j] * math.sin(2*math.pi*i*j/N)
    
    for i in range(N // 2):
        magn_arr[i] = (img_arr[i]**2 + real_arr[i]**2)**0.5

    idft = calc_idft(real_arr, img_arr)

    style.use('ggplot')
    main, plot_arr = pyplot.subplots(5, sharex=True)
    main.suptitle("Discrete Fourier Transform (DFT)")

    plot_arr[0].plot(source_signal)
    plot_arr[0].set_title("Input Signal")

    plot_arr[1].plot(real_arr)
    plot_arr[1].set_title("Real Part")

    plot_arr[2].plot(img_arr)
    plot_arr[2].set_title("Imaginary Part")

    plot_arr[3].plot(magn_arr)
    plot_arr[3].set_title("Magnitude")

    plot_arr[4].plot(idft)
    plot_arr[4].set_title("IDFT")

    pyplot.show()

def calc_idft(real_arr, img_arr):
    n = len(real_arr) 
    output = [0] * n * 2

    #normalize
    for i in range(n):
        real_arr[i] /= n
        img_arr[i] /= n
    
    for x in range(n*2):
        for y in range(n):
            output[x] += real_arr[y]*math.cos(2*math.pi*x*y/(n*2))
            output[x] += img_arr[y]*math.sin(2*math.pi*x*y/(n*2))
    return output

calc_dft(sigs.InputSignal_1kHz_15kHz)
