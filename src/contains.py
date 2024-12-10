import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import sys

def contains(superset, subset):
	if len(subset) > len(superset):
		print("Error: Subset must be smaller than superset")
		exit(-1)
	comparison = lowestDifference(superset, subset)
	print(comparison)
	return comparison


def lowestDifference(superset, subset):
	lowestDiff = sys.maxsize * 2 + 1
	# TODO this should have a much stricter cutoff. Experiment to find what that should be
	targetDiff = lowestDiff
	lowestIndex = 1

	options = len(superset) - len(subset) + 1
	for o in range(options):
		window = superset[o:o + len(subset)]
		diff = listDifference(window, subset)
		if o > 2335 and o < 2350:
			print(f"{o}, {diff}")
		if diff < lowestDiff:
			lowestDiff = diff
			lowestIndex = o

	if lowestDiff < targetDiff:
		return lowestDiff, lowestIndex
	else:
		return -1, -1


def listDifference(a, b):
	totalDiff = 0.0
	for i, j in zip(a, b):
		totalDiff += abs(i - j)
	return totalDiff


def windowContains(superset, subset):
	windows = sliding_window_view(superset, window_shape=len(subset))
	# Check if any window is equal to the subarray
	search = np.all(windows == subset, axis=1)
	result = np.any(search)
	print(len(subset))
	#print(subset[400:500])
	#print(superset[400:500])
	for i in range(len(search)):
		if search[i]:
			print(i)
	return result


def simpleContains(superset, subset):
	size = len(subset)
	if size > len(superset):
		print("Subset must be smaller than superset")
		exit(-1)
	for i in range(len(superset) - len(subset) + 1):
		if np.array_equal(superset[i:i+len(subset)], subset):
			return True
	return False

