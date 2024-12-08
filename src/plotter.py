import matplotlib.pyplot as plt
import numpy as np

def discreteTime(wav):
	numSamples = len(wav)
	plt.plot(wav)
	plt.show()
	return


def double(wav, zeros, ax):
	numSamples = len(wav)
	wavX = np.linspace(0, numSamples, num=numSamples)
	ax.plot(wav)
	zeroY = [0] * (len(zeros))
	ax.scatter(zeros, zeroY)

def both(wav1, zeros1, wav2, zeros2):
	fig, axis = plt.subplots(2)
	axis[0].set_title("bg")
	axis[1].set_title("sample")
	double(wav1, zeros1, axis[0])
	double(wav2, zeros2, axis[1])
	plt.show()
