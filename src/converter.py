import subprocess
from scipy.io import wavfile
import math
import wave

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