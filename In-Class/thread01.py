import threading

class MyThread(threading.Thread):
	def __init__(self, myId, count):
		self.myId = myId
		self.count = count
		threading.Thread.__init__(self)

	def run(self):
		for i in range(self.count):
			print("[%s] => %s" % (self.myId))