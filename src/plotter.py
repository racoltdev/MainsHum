import matplotlib.pyplot as plt
import numpy as np

def discreteTime(wav):
	numSamples = len(wav)
	plt.plot(wav)
	plt.show()
	return


def double(wav, zeros):
	numSamples = len(wav)
	wavX = np.linspace(0, numSamples, num=numSamples)
	plt.plot(wav)
	zeroY = [0] * (len(zeros))
	plt.scatter(zeros, zeroY)
	plt.show()
