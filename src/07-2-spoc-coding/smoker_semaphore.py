#coding=utf-8

import threading
import time
import random

class Seller(threading.Thread):
	def __init__(self, threadName, s, sad, sbd, scd):
		threading.Thread.__init__(self, name=threadName)
		self.sleepTime = 1
		self.s = s
		self.sad = sad
		self.sbd = sbd
		self.scd = scd

	def run(self):
		while True:
			self.s.acquire()
			r = random.randint(1, 3)
			if r == 1:
				print 'Sell paper and matches. '
				self.sad.release()
			elif r == 2:
				print 'Sell tobacco and matches. '
				self.sbd.release()
			elif r == 3:
				print 'Sell paper and tobacco. '
				self.scd.release()
			self.s.release()
			time.sleep(self.sleepTime)

class Smoker(threading.Thread):
	def __init__(self, threadName, s, sabc):
		threading.Thread.__init__(self, name=threadName)
		self.sleepTime = 1
		self.s = s
		self.sabc = sabc

	def run(self):
		while True:
			self.sabc.acquire()
			if self.name == 'A':
				print 'Fetching paper and matches. '
			elif self.name == 'B':
				print 'Fetching tabacco and matches. '
			else:
				print 'Fetching paper and tabacco. '
			self.s.release()
			print 'Smoker %s is smoking. ' %(self.name)
			time.sleep(self.sleepTime)

s = threading.Semaphore(1)
sad = threading.Semaphore(0)
sbd = threading.Semaphore(0)
scd = threading.Semaphore(0)

seller = Seller("D", s, sad, sbd, scd)
smoker_a = Smoker("A", s, sad)
smoker_b = Smoker("B", s, sbd)
smoker_c = Smoker("C", s, scd)
seller.start()
smoker_a.start()
smoker_b.start()
smoker_c.start()
