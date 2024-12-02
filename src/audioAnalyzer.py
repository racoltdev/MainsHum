import numpy as np
import scipy.signal as sig
import math

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

	data, sample_rate = down_sample(data, sample_rate, freq_min, freq_max)
	# Fall off rate of frequencies outside the range
	order = 5
	bandpass_filter = lambda d : butter_bandpass(d, freq_min, freq_max, sample_rate, order)
	pass_through = np.apply_along_axis(bandpass_filter, 0, data).astype('int16')
	output = normalize(pass_through)
	return output, sample_rate


def down_sample(data, sample_rate, freq_min, freq_max):
	band = freq_max - freq_min

	if band > (0.005 * sample_rate):
		print("\tDown sampling not needed. Band is wide enough")
		return data, sample_rate

	# Yeah, this is magic, but it's just a random eq to get a roughly ok sampling rate
	# Desired is at least 1 order of magnitude greater than freq_max
	desired_rate = int(10 ** math.ceil(np.log10(freq_max)) * 1.5)

	factor = int(sample_rate / desired_rate)

	# Final sample rate will not be exactly the desired rate because the factor must be an int
	print(f"\tDownsampling from {sample_rate}Hz to ~{desired_rate}Hz")
	# This sucks
	# decimate should only be done with a factor of 13 max at a time
	# this is the best I could come up with to step with decimate
	while factor >= 10:
		factor /= 10
		sample_rate /= 10
		data = sig.decimate(data, 10, axis=0)

	# Must keep type cast of factor and sample_rate in sync
	factor = int(np.round(factor))
	if factor > 1:
		sample_rate = int(np.round(sample_rate / factor))
		data = sig.decimate(data, factor, axis=0)

	return data, int(np.round(sample_rate))


def butter_bandpass(data, low_cut, high_cut, sample_rate, order):
	# Not sure why, but nyq isn't needed here, and frequencies are expected in Hz. ¯\_(ツ)_/¯
	# nyq freq is half the sample rate.
	# It's the highest freq that can be captured at a sample rate
	#nyq = 0.5 * sample_rate
	#low = low_cut / nyq
	#high = high_cut / nyq

	# sos is the best method to use. ba breaks a lot with low ranges
	sos = sig.butter(order, [low_cut, high_cut], btype='bandpass', output='sos', fs=sample_rate)
	# Calculate what passes through the filter
	return sig.sosfilt(sos, data)


# This just assumes desired output volume is around 600 since thats what most of my samples were at. 60 Hz is audible to me with this volume
def normalize(output):
	o_avg = np.average(np.absolute(output))
	target_volume = 600
	factor = round(target_volume / o_avg)
	return output * factor
