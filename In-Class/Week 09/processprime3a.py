# processprime3.py
# program to use multiple processes to find prime factors of a group
# of numbers, demonstrating the use of queues as well as showing
# how threads compare to processes by way of the counterpart program
# threadprime2.py
# This version uses process pools

import math
from multiprocessing import Process, Pool

def primeFactors(n):
	result = []

	# get all the twos if this number is even
	while n % 2 == 0:
		result.append(2)
		n = n / 2

	# at this point in time, n must be odd, so we can
	# count from 3 to the int(sqrt(n))+1 by 2s for other numbers to try
	for i in range(3, int(math.sqrt(n))+1, 2):

		# while i divides n, add i to list and divide
		while n % i == 0:
			result.append(i)
			n = n / i

	# if n is prime, we land here, unless n is finally 1 or 0
	if n > 2:
		result.append(n)

	return result

def worker(n):
	a = primeFactors(n)
	# print "Prime factors of {0} are {1}".format(n, a)

if __name__ == "__main__":
	pool = Pool(processes=10)

	pool.map(worker,range(2,500000))
