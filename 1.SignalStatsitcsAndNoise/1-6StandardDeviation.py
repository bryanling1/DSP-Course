import numpy as np
import mysignals as sigs

standard_deviation = np.std(sigs.InputSignal_1kHz_15kHz)
print(standard_deviation)

def calc_variance(signal_array):
    mean = 0.0
    variance = 0.0

    for x in range(len(signal_array)):
        mean += signal_array[x]

    mean /= len(signal_array)

    for x in range(len(signal_array)):
        variance += (signal_array[x] - mean)**2
    
    variance /= len(signal_array)
    return variance

def cal_standard_deviation(signal_array):
    return calc_variance(signal_array) ** 0.5


print(cal_standard_deviation(sigs.InputSignal_1kHz_15kHz))









