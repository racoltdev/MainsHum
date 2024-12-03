import os
import re

def isFloat(s):
	if re.match(r'^(\d+)?(\.\d+)?$', s) is None or not s:
		return False
	else:
		return True


def outputExists(output_file):
	if os.path.isfile(output_file):
		prompt = input(f"Warning, output file \"{output_file}\" already exists. Over write? y/n\n")
		if prompt.lower()[0] != 'y':
			print("Aborting")
			exit(-1)
	return


def assertFileExists(file):
	if not os.path.isfile(file):
		print("error")
		exit(-1)
	return


def getFreqBounds(freq, freq_range, FREQ_MIN, FREQ_MAX):
	if isFloat(freq) and float(freq) >= FREQ_MIN and float(freq) <= FREQ_MAX:
		freq = float(freq)
	else:
		print("Frequency must be a positive number between {FREQ_MIN} and {FREQ_MAX}")
		exit(-1)

	if isFloat(freq_range):
		freq_range = float(freq_range)
		freq_min = max(FREQ_MIN, freq - freq_range)
		freq_max = min(FREQ_MAX, freq + freq_range)
	else:
		print("Frequency range error")
		exit(-1)

	return freq_min, freq_max
