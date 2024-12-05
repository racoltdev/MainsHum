import subprocess
from scipy.io import wavfile
import math

# TODO enable reading from a wav stream instead. Need to find a way to convert a stream to np array
def toWav(filename, newName, stdout=False):
	command = f"ffmpeg -loglevel level+warning -i \"{filename}\" \"{newName}\""
	if stdout:
		command = f"ffmpeg -loglevel level+warning -i \"{filename}\" -f wav pipe:1"

    # "check" means raise exception if command fails
	subprocess.check_output(command, shell=True)
	return


def wavToNp(filename):
	sample_rate, data = wavfile.read(filename)
	return sample_rate, data


def HzToRads(freq):
	return 2 * math.pi * freq


def listDelta(l):
	return [l[x + 1] - l[x] for x in range(len(l) - 1)]


def toMono(wav):
	mono = wav
	channels = len(wav[0])
	if channels > 0:
		mono = [x[0] for x in wav]
	return mono
