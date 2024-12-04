import os
from scipy.io import wavfile

import audioAnalyzer
import converter
import cli_utils as util

# Only for use internally in this program. Do not call this directly while scripting or handling user input
# sample can be any filename with audio data
def extract(sample, freq_min, freq_max):
	print(f'\tSample file: {os.path.abspath(sample)}\n\tFrequency band: [{freq_min}, {freq_max}]\n')

	wav = sample
	useTemp = False
	if os.path.splitext(sample)[1] != ".wav":
		#Isolate just the name of the file
		tmpFile = os.path.split(sample)[1]
		tmpFile = os.path.splitext(tmpFile)[0] + ".tmp.wav"

		print(f'\tCreating temporary {tmpFile}')
		converter.toWav(sample, tmpFile)

		wav = tmpFile
		useTemp = True

	print(f'\tAttempting to extract frequency band from {sample}')
	extracted, sample_rate = audioAnalyzer.freqExtract(wav, freq_min, freq_max)

	print(f'\tSuccessfully extracted from {sample}')

	if useTemp:
		print('\tRemoving temporary file')
		os.remove(wav)

	return sample_rate, extracted


# If dealing with user input, call this
# This cleans up input and verifies its good
# sample can be any filename with audio data
def extract_cli(sample, freq, freq_range, output_file):
	# TODO min and max should be calculated based off of sample_rate
	FREQ_MIN = 20.0
	FREQ_MAX = 20000.0

	util.assertFileExists(sample)
	# Leave determining if its an audio file to ffmpeg. It will know better than I do

	util.promptOutputExists(output_file)

	freq_min, freq_max = util.getFreqBounds(freq, freq_range, FREQ_MIN, FREQ_MAX)

	sample_rate, extracted = extract(sample, freq_min, freq_max)
	print(f"\tSaving to {output_file}")
	wavfile.write(output_file, sample_rate, extracted)
	return
