import math
import time
import sys

from time import sleep, time
from threading import Thread

def asynchronus(fun, *args, **keyword):
	# custom async fn
	thread = Thread(None, fun, None, args)
	if "autorun" in keyword or len(keyword) == 0:
		thread.start()

	return thread

class Timer(Thread):
	# lets users run events relative to each other
	def __init__(self):
		self.queue = {}
		Thread.__init__(self)
		return

	def append(self, reltime, fun, *args):
		self.queue[time()+reltime, fun, *args]
		return

class Go:
	def __init__(self):
		return

	def move(self):
		# move forward one second at default speed
		return

	def move(self, dir):
		# move in <dir> one second at default speed
		return
	
	def move(self, dir, speed):
		# move in <dir> one second at <speed> speed
		return
	
	def move(self, dir, dist):
		# move in <dir> <dist> at default speed
		return
	
	def move(self, dir, speed, dist):
		# move in <dir> <dist> at <speed> speed
		return

class Blink:
	def __init__(self):
		return

class LCD:
	def __init__(self):
		return

	def write(self, text):
		# outputs `text' to lsd
		return

def setup():
	# define classes and functions
	lcd = LCD()
	terminal = sys.stdout
	sys.stdout=lcd   # redirect standard output to the lcd through the class method write(text)

	try:
		fin = open("user.gg", "r")
		data = fin.read()
		fin.close()
	except:
		print "File \"user.gg\" not found. Balls!"
		return 1

	try:
		exec(data)
	except Exception:
		print Exception
		return 1
	return 0

if __name__=="__main__":
	setup()

