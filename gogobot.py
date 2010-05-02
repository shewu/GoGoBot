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
	
# Arduino is currently contained in startscript.py
Left=-1
Right=1
class Arduino:
    def __init__(self, dev, baud=9600):
        return
    def send(head, bytes):
        return
    def motor(side, speed):
        return

class Timer(Thread):
	# lets users run events relative to each other
	def __init__(self):
		self.queue = {}    # change queue into a self sorting data struct
		Thread.__init__(self)
		return
		
	def run(self):
	    while 1:
	        t = time()
	        for event,(function,args) in self.queue:
	            if event<=t:
	                asynchronus(function,*args)
                del self.queue[event]

	def append(self, reltime, fun, *args):
		self.queue[time()+reltime]=(fun, *args)
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
		
# basic user functions - easy to use functions for beginners
# ---------------------
def go(speed,angle=0):
    pass
def stop():
    pass
def gofor(timems,speed):
    pass
def turn(angle):
    pass
# will call 'function' with the arguments in 'args' after 'timems' miliseconds
def timed(timems,function,*args):
    pass
# returns a float in degrees
def compass():
    pass
# returns a float distance from any IR sensor in cm
# 'IR' is the sensor pin (or id number)
def distance(IR):
    pass
# ---------------------

# internal functions - user will not need to use these functions directly
# ---------------------

# cycles through usb drivers till arduino is found
def _find_arduino(dev = '/dev/ttyUSB',start=0,stop=2):
    for i in range(start,stop+1):
        try:
            a = Arduino(dev+str(i))
            head,body = a.send(INIT, 0)
            # INIT not implimented yet
            # should return a sequence that is unique to the gogobot arduino program
# ---------------------

def setup():
	# define classes and functions
	arduino = Arduino()
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

