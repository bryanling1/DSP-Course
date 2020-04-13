import numpy as np
from scipy import signal

sig = np.array([0,0,0,0,1,1,1,1])
filter = np.array([1,1,0])

conv_result = signal.convolve(sig, filter)
dconv_result = signal.deconvolve(conv_result, filter)

print("Convolution result:")
print(conv_result)
print("Deconvolution result:")
print(dconv_result)


