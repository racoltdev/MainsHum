import subprocess
from scipy.io import wavfile
import math

def toWav(filename, newName):
	command = f"ffmpeg -loglevel level+warning -i \"{filename}\" \"{newName}\""
	subprocess.run(command, shell=True, check=True)

def wavToNp(filename):
	sample_rate, data = wavfile.read(filename)
	return sample_rate, data

def HzToRads(freq):
	return 2 * math.pi * freq
