import cli_utils as util
import extract
import converter
import plotter

def compare(sample, background, freq_min, freq_max):
	sample_rate, extracted = extract.extract(sample, freq_min, freq_max)
	bg_sample_rate, bg = converter.wavToNp(background)

	print(f"\n\tConverting samples to mono")
	bg_mono = converter.toMono(bg)
	sample_mono = converter.toMono(extracted)

	#plotter.discreteTime(sample_mono)

	bg_zeros = getZeros(bg_mono)
	#bg_lengths = converter.listDelta(bg_zeros)
	plotter.double(bg_mono, bg_zeros)
	#sample_zeros = getZeros(sample_mono)
	#sample_lengths = converter.listDelta(sample_zeros)
	return


def getZeros(wav):
	sign = getSign(wav[0])
	zeros = []
	zerosInARow = []
	for i in range(len(wav)):
		# Catch if sample is exactly 0
		# Does not need fuzzy matching since values are int16
		if wav[i] == 0:
			zerosInARow.append(i)
		elif getSign(wav[i]) != sign:
			sign = not sign
			# Assume portion of the sine wave near zero is approx linear
			# This is a valid assumption is there are at least 10 samples per wavelength
			portion = 0.0
			if wav[i - 1] == 0:
				portion = lin_interpolate(zerosInARow[0], i - 1)
				zerosInARow = []
			else:
				portion = lin_interpolate(wav[i - 1], wav[i])
			zeros.append(float(i - 1) + portion)
	return zeros


# Returns the distance from u as a proportion of (v - u) where a line would intersect y=0
def lin_interpolate(u, v):
	# Avoid division by zero
	if (u == v):
		return 0
	slope = (v - u)
	intercept = - u / slope
	return intercept


def getSign(x):
	return False if x < 0 else True


def almostEquals(x, y, fuzz=0.0005):
	return (y < x + fuzz) & (y > x - fuzz)


# Sample should not be processed before being passed
def compare_cli(sample, background, freq, freq_range):
	FREQ_MIN = 20.0
	FREQ_MAX = 20000.0

	util.assertFileExists(sample)
	util.assertFileExists(background)

	freq_min, freq_max = util.getFreqBounds(freq, freq_range, FREQ_MIN, FREQ_MAX)

	compare(sample, background, freq_min, freq_max)
	return
