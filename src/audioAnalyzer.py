import numpy as np
import scipy

import audioConverter

# Assume data being passes is a wav file

"""
sample: string, .wav filename
freq_min, freq_max : float, min and max freqs of the filter in Hz
returns raw data from a bandpass
"""
def freqExtract(sample, freq_min, freq_max):
	sample_rate, data = audioConverter.wavToNp(sample)
	low_cut = audioConverter.HzToRads(freq_min)
	high_cut = audioConverter.HzToRads(freq_max)

	# Fall off rate of frequencies outside the range
	order = 5
	bandpass_filter = lambda d : butter_bandpass(d, low_cut, high_cut, sample_rate, order)
	pass_through = np.apply_along_axis(bandpass_filter, 0, data).astype('int16')
	return pass_through, sample_rate


def butter_bandpass(data, low_cut, high_cut, sample_rate, order):
	# nyq freq is half the sample rate.
	# It's the highest freq that can be captured at a sample rate
	nyq = 0.5 * sample_rate
	low = low_cut / nyq
	high = high_cut / nyq

	# TODO Should play around with different output options to see which is best
	# Creat the filter
	b, a = scipy.signal.butter(order, [low, high], btype='bandpass', output='ba', fs=sample_rate)
	# Calculate what passes through the filter
	return scipy.signal.lfilter(b, a, data)
