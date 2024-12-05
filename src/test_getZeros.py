import numpy as np

import compare

wav = [np.int16(8), np.int16(10), np.int16(11), np.int16(11), np.int16(9), np.int16(6), np.int16(3), np.int16(0), np.int16(-4), np.int16(-7), np.int16(-10), np.int16(-11), np.int16(-11), np.int16(-9), np.int16(-7), np.int16(-3), np.int16(0), np.int16(3), np.int16(7), np.int16(9), np.int16(11), np.int16(11), np.int16(10), np.int16(7), np.int16(4), np.int16(0), np.int16(-3), np.int16(-6), np.int16(-9), np.int16(-10), np.int16(-11), np.int16(-10), np.int16(-8), np.int16(-5), np.int16(-1), np.int16(2), np.int16(6), np.int16(8), np.int16(10), np.int16(11), np.int16(10), np.int16(8), np.int16(5), np.int16(2), np.int16(-1), np.int16(-5), np.int16(-8), np.int16(-10), np.int16(-11), np.int16(-10), np.int16(-8), np.int16(-6), np.int16(-2), np.int16(1), np.int16(4), np.int16(7), np.int16(10), np.int16(11), np.int16(10), np.int16(9), np.int16(6), np.int16(3), np.int16(0), np.int16(-4), np.int16(-7), np.int16(-9), np.int16(-10), np.int16(-10), np.int16(-9), np.int16(-6), np.int16(-3), np.int16(0), np.int16(3), np.int16(6), np.int16(9), np.int16(10), np.int16(10), np.int16(9), np.int16(7), np.int16(4), np.int16(0), np.int16(-3), np.int16(-6), np.int16(-8), np.int16(-10), np.int16(-10), np.int16(-9), np.int16(-7), np.int16(-4), np.int16(-1), np.int16(2), np.int16(5), np.int16(8), np.int16(10), np.int16(10), np.int16(9), np.int16(7), np.int16(5), np.int16(1), np.int16(-1)]

z = compare.getZeros(wav)
expected = [7.0, 16.0, 25.0, np.float64(34.333333333333336), np.float64(43.666666666666664), np.float64(52.666666666666664), 62.0, 71.0, 80.0, np.float64(89.33333333333333), np.float64(98.5)]
if z == expected:
	print("pass")
else:
	print("fail")
