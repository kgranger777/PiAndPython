# process02.py
# part of a two-program demo with thread04.py to show the difference
# between threads and processes.

import os
from multiprocessing import Process, Lock 

def doubler(number, lock):
	# a simple function to use to demonstrate multiprocessing
	result = number * 2
	proc = os.getpid()
	with lock:
		print("{0} doubled to {1} by process id: {2}".format(number, result, proc))

if __name__ == "__main__":
	numbers = [5, 10, 15, 20, 25]
	procs = []
	lock = Lock()

	for number in numbers:
		proc = Process(target=doubler, args=(number,lock))
		procs.append(proc)
		proc.start()

	for proc in procs:
		proc.join()
