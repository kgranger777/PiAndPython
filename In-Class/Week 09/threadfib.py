# threadprime.py
# program to use multiple threads to find prime factors of a group
# of numbers, demonstrating the use of queues as well as showing
# how threads compare to processes by way of the counterpart program
# processprime.py

import math
from Queue import Queue
from threading import Thread
import sys

def fib(n):
	if n <= 1:
		return 1
	else:
		return fib(n-2) + fib(n-1)

def worker():
	while True:
		n = q.get()
		a = fib(n)
		q.task_done()
		print "Number {0} fibonacci number is {1}".format(n, a)

q = []

if __name__ == "__main__":
	q = Queue()
	n = int(sys.argv[1])
	for i in range(n):
		t = Thread(target=worker)
		t.daemon = True
		t.start()

	for i in range(40):
		q.put(i)

	q.join()
