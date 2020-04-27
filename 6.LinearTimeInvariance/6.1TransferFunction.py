from scipy import signal
import numpy as np 

#trasnfer function H(s) = s^2+3s+3/s^2+2s+1

numerators = [1, 3, 3]
denominators = [1, 2, 1]

H1 = signal.TransferFunction(numerators, denominators)
print(H1)

#discrete transfer function with a sampling rate of 0.1
#we use z instead of s
#H(z) = z^2+3z+3/z^2+2z+1

H2 = signal.TransferFunction(numerators, denominators, dt=0.1)
print(H2)