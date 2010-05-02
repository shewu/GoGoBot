import math
import time

from time import sleep
from threading import Thread

class Async(Thread):
	def __init__(self, fun, *args):
		Thread.__init__(self)
		self.fun = fun
		self.args = args
		self.halt = False
		return
	
	def run():
		self.fun(*self.args)
		return
	
	def stop():
		return

def asynchronus(fun, *args):
	# custom async fn
	return

class Go:
	def __init__(self):
		return

	def move():
		# move forward one unit at default speed
		return

	def move(dir):
		# move in <dir> one unit at default speed
		return
	
	def move(dir, speed):
		# move in <dir> one unit at <speed> speed
		return
	
	def move(dir, dist):
		# move in <dir> <dist> at default speed
		return
	
	def move(dir, speed, dist):
		# move in <dir> <dist> at <speed> speed
		return

class Blink:
	def __init__(self):
		return

class LCD:
	def __init__(self):
		return

	def output(text):
		# outputs `text' to lsd
		return

def setup():
	# define classes and functions
	lcd = LCD()

	try:
		fin = open("user.gg", "r")
		data = fin.read()
		fin.close()
	except:
		lcd.output("File \"user.gg\" not found. Balls!")
		return 1

	try:
		exec(data)
	except Exception:
		lcd.output(Exception)
		return 1
	return 0

if __name__=="__main__":
	setup()

