# process01.py
# part of a two-program demo with thread03.py to show the difference
# between threads and processes.

import os
from multiprocessing import Process 

def doubler(number):
	# a simple function to use to demonstrate multiprocessing
	result = number * 2
	proc = os.getpid()
	print("{0} doubled to {1} by process id: {2}".format(number, result, proc))

if __name__ == "__main__":
	numbers = [5, 10, 15, 20, 25]
	procs = []

	for number in numbers:
		proc = Process(target=doubler, args=(number,))
		procs.append(proc)
		proc.start()

	for proc in procs:
		proc.join()
