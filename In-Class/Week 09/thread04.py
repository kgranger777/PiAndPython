# thread04.py
# part of a two-program demo with process02.py to show the difference
# between threads and processes.

import os
from threading import Thread, Lock

def doubler(number,lock):
	# a simple function to use to demonstrate multiprocessing
	result = number * 2
	proc = os.getpid()
	with lock:
		print("{0} doubled to {1} by process id: {2}".format(number, result, proc))

if __name__ == "__main__":
	numbers = [5, 10, 15, 20, 25]
	threads = []
	lock = Lock()

	for number in numbers:
		thread = Thread(target=doubler, args=(number,lock))
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()
