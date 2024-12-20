import sys
import os

import extract
import compare

def cli_main(args):
	mode = args[0]
	args = args[1:]
	mode = mode.lower()

	if mode == "extract" or mode == "x":
		print("Extracting...")
		extract.extract_cli(*args)
		print("Done!")
	elif mode == "compare" or mode == "c":
		print("Comparing...")
		compare.compare_cli(*args)
		print("Done!")
	else:
		help()

	return


def help():
	print("help text")
	exit(-1)


def extractError(args, e):
		print(args)
		print(str(e))
		exit(-1)


if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) == 0:
		help()
	cli_main(args)
