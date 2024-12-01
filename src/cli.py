import sys
import os

import extract

def cli_main(args):
	mode = args[0]
	args = args[1:]
	mode = mode.lower()

	if mode == "extract" or mode == "x":
		print("Extacting...")
		extract.extract(*args)
		print("Done!")
	elif mode == "compare" or mode == "c":
			compare(*args)
	else:
		help()

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


if __name__ == "__main__":
	args = sys.argv[1:]
	if len(args) == 0:
		help()
	cli_main(args)
