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
	#low_cut = audioConverter.HzToRads(freq_min)
	#high_cut = audioConverter.HzToRads(freq_max)

	# Fall off rate of frequencies outside the range
	order = 5
	bandpass_filter = lambda d : butter_bandpass(d, freq_min, freq_max, sample_rate, order)
	pass_through = np.apply_along_axis(bandpass_filter, 0, data).astype('int16')
	output = normalize(pass_through)
	return output, sample_rate


def butter_bandpass(data, low_cut, high_cut, sample_rate, order):
	# Not sure why, but nyq isn't needed here, and frequencies are expected in Hz. ¯\_(ツ)_/¯
	# nyq freq is half the sample rate.
	# It's the highest freq that can be captured at a sample rate
	#nyq = 0.5 * sample_rate
	#low = low_cut / nyq
	#high = high_cut / nyq

	# sos is the best method to use. ba breaks a lot with low ranges
	sos = scipy.signal.butter(order, [low_cut, high_cut], btype='bandpass', output='sos', fs=sample_rate)
	# Calculate what passes through the filter
	return scipy.signal.sosfilt(sos, data)


# This just assumes desired output volume is around 600 since thats what most of my samples were at. 60 Hz is audible to me with this volume
def normalize(output):
	o_avg = np.average(np.absolute(output))
	target_volume = 600
	factor = round(target_volume / o_avg)
	return output * factor


