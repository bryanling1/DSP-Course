import numpy as np 
import scipy.signal as signal
from matplotlib import pyplot
from matplotlib import style

#signal samplying rate of 2000Hz, ntq = 1000Hz

t = np.linspace(0, 1, 2001)

sig_5hz = np.sin(2*np.pi*5*t)
sig_50hz = np.sin(2*np.pi*50*t)
sig_250hz = np.sin(2*np.pi*250*t)
sig_5hz_50hz_250hz = sig_5hz + sig_50hz + sig_250hz

numtaps = 101
lpf_cutoff = 7
hpf_cutoff = 100
bp_cutoff1 = 40
bp_cutoff2 = 100

#lowpass
lowpass_coefficient = signal.firwin(numtaps, lpf_cutoff, nyq=1000)
lowpass_output = signal.convolve(sig_5hz_50hz_250hz, lowpass_coefficient, mode="same")

#highpass
highpass_coefficient = signal.firwin(numtaps, hpf_cutoff, pass_zero=False, nyq=1000)
highpass_output = signal.convolve(sig_5hz_50hz_250hz, highpass_coefficient, mode="same")

#bandpass 
bandpass_coefficient = signal.firwin(numtaps, [bp_cutoff1, bp_cutoff2], pass_zero=False, nyq=1000)
bandpass_output = signal.convolve(sig_5hz_50hz_250hz, bandpass_coefficient, mode="same")

pyplot.plot(bandpass_output)
pyplot.show()

