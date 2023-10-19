# thread01.py
# mostly copied from the book Programming Python, 4th Ed.

import threading

class MyThread(threading.Thread):
	def __init__(self, myId, count):
		self.myId = myId
		self.count = count
		threading.Thread.__init__(self)

	def run(self):
		for i in range(self.count):
			print "[%s] => %s" % (self.myId, i)

threads = []
for i in range(10):
	thread = MyThread(i, 100)
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()
print "Main thread exiting"
