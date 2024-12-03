import os

import cli_utils as util
import extract
import converter

def compare(sample, background, freq_min, freq_max):
	sample_rate, extracted = extract.extract(sample, freq_min, freq_max)
	bg = converter.wavToNp(background)
	return


# Sample should not be processed before being passed
def compare_cli(sample, background, freq, freq_range):
	FREQ_MIN = 20.0
	FREQ_MAX = 20000.0

	util.assertFileExists(sample)
	util.assertFileExists(background)

	freq_min, freq_max = util.getFreqBounds(freq, freq_range, FREQ_MIN, FREQ_MAX)

	compare(sample, background, freq_min, freq_max)
	return
