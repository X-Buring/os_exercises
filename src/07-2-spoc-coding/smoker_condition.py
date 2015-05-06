#coding=utf-8

'''
flag 用于表示桌上的情况，即现在 flag 号吸烟者可以吸烟
0 代表桌上什么也没有
'''

import threading 
import time
import random

# mutex = threading.Semaphore(1)
condition = threading.Condition()
flag = 0

class Seller(threading.Thread):
	def __init__(self, threadName):
		threading.Thread.__init__(self, name=threadName)

	def run(self):
		global condition, flag
		print 'I am seller. '
		while True:
			if condition.acquire():
				if flag == 0:
					flag = random.randint(1, 3)
					if flag == 1:
						print 'Sell paper and matches. '
					elif flag == 2:
						print 'Sell tobacco and matches. '
					elif flag == 3:
						print 'Sell paper and tobacco. '
					condition.notifyAll()
				else:
					condition.wait()
				condition.release()

class Smoker(threading.Thread):
	def __init__(self, threadName, index):
		threading.Thread.__init__(self, name=threadName)
		self.index = index

	def run(self):
		global condition, flag
		print 'I am smoker %d. ' %(self.index)
		while True:
			if condition.acquire():
				if flag == self.index:
					if self.index == 1:
						print 'Fetching paper and matches. '
					elif self.index == 2:
						print 'Fetching tabacco and matches. '
					elif self.index == 3:
						print 'Fetching paper and tabacco. '
					print 'Smoker %s is smoking. ' %(self.name)
					time.sleep(1)
					flag = 0
					condition.notifyAll()
			else:
				condition.wait()
			condition.release()


seller = Seller('D')
smoker1 = Smoker('A', 1)
smoker2 = Smoker('B', 2)
smoker3 = Smoker('C', 3)

seller.start()
smoker1.start()
smoker2.start()
smoker3.start()


