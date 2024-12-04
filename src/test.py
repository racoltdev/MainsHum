import random
import numpy as np


def main():
	random.seed()
	iters = 1000000
	step = 5.31

	max_error = 0
	worst_factor = 0
	for _ in range(iters):
		i = random.randint(1, 1000)
		d = random.random()
		o_factor = i + d
		#o_factor = 12.5
		factor = o_factor
		#print(factor)
		real_factor = 1
		while factor >= step:
			factor /= step
			real_factor *= step
			#print(f"Desired Factor: {factor}")
			#print(f"Actual Factor: {real_factor}")

		# Must keep type cast of factor and sample_rate in sync
		factor = int(np.round(factor))
		if factor > 1:
			real_factor *= factor
			#print(f"Desired Factor: {factor}")
			#print(f"Actual Factor: {real_factor}")

		error = np.absolute(o_factor - real_factor) / o_factor
		if error > max_error:
			worst_factor = o_factor
			max_error = error
		#print(f"Desired Factor: {o_factor}")
		#print(f"Actual Factor: {real_factor}")
		#print(f"Error percent: {error}")
	print(f"Max error: {max_error}")
	print(f"Worst factor: {worst_factor}")

if __name__ == "__main__":
	main()
