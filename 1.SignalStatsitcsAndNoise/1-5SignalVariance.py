import numpy as np
import mysignals as sigs

variance = np.var(sigs.InputSignal_1kHz_15kHz)
print(variance)

#manual function
def calc_variance(signal_array):
    mean = 0.0;
    variance = 0.0;

    for x in range(len(signal_array)):
        mean += signal_array[x]

    mean /= len(signal_array)

    for x in range(len(signal_array)):
        variance += (signal_array[x] - mean)**2
    
    variance /= len(signal_array)
    return variance

print(calc_variance(sigs.InputSignal_1kHz_15kHz))








