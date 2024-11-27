import os
import re
from scipy.io import wavfile

import audioConverter
import audioAnalyzer

def extract(sample, freq, freq_range, output_file):
	FREQ_MIN = 20
	FREQ_MAX = 40000

	freq, freq_min, freq_max = _cleanArgs(sample, freq, freq_range, output_file, FREQ_MIN, FREQ_MAX)

	print(f'\tSample file: {os.path.abspath(sample)}\n\tFrequency band: [{freq_min}, {freq_max}]\n')

	wav = sample
	useTemp = False
	if os.path.splitext(sample)[1] != ".wav":
		#Isolate just the name of the file
		tmpFile = os.path.split(sample)[1]
		tmpFile = os.path.splitext(tmpFile)[0] + "tmp.wav"

		print(f'\tCreating temporary {tmpFile}')
		audioConverter.toWav(sample, tmpFile)

		wav = tmpFile
		useTemp = True

	print(f'\tAttempting to extract frequency band from {sample}')
	extracted, sample_rate = audioAnalyzer.freqExtract(wav, freq_min, freq_max)

	print(f'\tSuccessfully extracted from {sample}\n\tSaving to {output_file}')
	wavfile.write(output_file, sample_rate, extracted)

	if useTemp:
		print('\tRemoving temporary file')
		os.remove(wav)
	return


def _cleanArgs(sample, freq, freq_range, output_file, FREQ_MIN, FREQ_MAX):
	if not os.path.isfile(sample):
		print("error")
		exit()
	# Leave determining if its an audio file to ffmpeg. It will know better

	if os.path.isfile(output_file):
		prompt = input("Warning, output file already exists. Over write? y/n\n")
		if prompt.lower()[0] != 'y':
			print("Aborting")
			exit()

	if isFloat(freq) and float(freq) >= FREQ_MIN and float(freq) <= FREQ_MAX:
		freq = float(freq)
	else:
		print("Frequency must be a positive number between {FREQ_MIN} and {FREQ_MAX}")
		exit()

	if isFloat(freq_range):
		freq_range = float(freq_range)
		freq_min = max(FREQ_MIN, freq - freq_range)
		freq_max = min(FREQ_MAX, freq + freq_range)
	else:
		print("Frequency range error")
		exit()

	return freq, freq_min, freq_max


def isFloat(s):
	if re.match(r'^\d+(\.(\d?)+)?$', s) is None:
		return False
	else:
		return True
