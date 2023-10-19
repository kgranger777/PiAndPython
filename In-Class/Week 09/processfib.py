# processprime3.py
# program to use multiple processes to find prime factors of a group
# of numbers, demonstrating the use of queues as well as showing
# how threads compare to processes by way of the counterpart program
# threadprime2.py
# This version uses process pools

import math
import sys
from multiprocessing import Pool

def fib(n):
	if n <= 1:
		return 1
	else:
		return fib(n-2) + fib(n-1)

def worker(n):
	a = fib(n)
	print "Fibonacci number number {0} is {1}".format(n, a)

if __name__ == "__main__":
	nrp = int(sys.argv[1])
	pool = Pool(processes=nrp)

	pool.map(worker,range(40))
	print "Number of processes = {0}".format(nrp)
