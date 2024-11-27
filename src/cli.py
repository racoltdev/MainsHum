import sys
import os
import re

import audioConverter
import audioAnalyzer


def cli_main(args):
	mode = args[0]
	args = args[1:]
	mode = mode.lower()

	if mode == "extract" or mode == "x":
		extract(*args)
	elif mode == "compare" or mode == "c":
			compare(*args)
	else:
		help()

	return


def extract(sample, freq, freq_range, output_file):
	FREQ_MIN = 20
	FREQ_MAX = 40000

	freq_min, freq_max = 0, 0

	if not os.path.isfile(sample):
		print("error")
		exit()
	# Leave determining if its an audio file to ffmpeg. It will know better

	if os.path.isfile(output_file):
		prompt = input("Warning, output file already exists. Over write? y/n")
		if prompt.lower()[0] != 'y':
			print("Aborting")

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
	print(sample, freq, freq_min, freq_max, output_file)

	#Isolate just the name of the file
	newName = os.path.split(sample)[1]
	newName = os.path.splitext(newName)[0] + "tmp.wav"
	audioConverter.toWav(sample, newName)

	audioAnalyzer.freqExtract(newName, freq_min, freq_max)

	return


def compare(sample, history):
	if not os.path.isfile(sample):
		print("error")
	if not os.path.isfile(history):
		print("error")
	print(sample, history)


def help():
	print("help text")
	exit()


def extractError(args, e):
		print(args)
		print(str(e))
		exit()


def isFloat(s):
	if re.match(r'^\d+(\.(\d?)+)?$', s) is None:
		return False
	else:
		return True


if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) == 0:
		help()
	cli_main(args)
