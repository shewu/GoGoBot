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
	
# basic user functions - easy to use functions for beginners
# ---------------------
# if we have these functions then i can just get rid of the ``go'' class
def go(speed,angle=0):
	return

def stop():
	return

def gofor(timems,speed):
	return

def turn(angle):
	# what about radius?
	return

ON = 1, OFF = 0

def light(state, time):
	if state == 1:
		return
	else: # state == 0
		return

def blink(time):
	# blinking the light on the arduino
	return

def display(text):
	# displaying text on the LCD
	return

def delayRun(timems,function,*args):
	# will call `function' with the arguments in `args' after `timems' milliseconds
	return

def getDirection():
	# returns a float in degrees
	return

def getDistance(IR):
	# returns a float distance from any IR censor in cm
	# `IR' isi the sensor pin (or id number)
	return
# ---------------------

# internal functions - user will not need to use these functions directly
# ---------------------

def _find_arduino(dev = '/dev/ttyUSB',start=0,stop=2):
	# cycles through usb drivers until arduino is found
    for i in range(start,stop+1):
        try:
            serial = dev+str(i)
            a = Arduino(serial)
            head,body = a.send(INIT, 0)
            # INIT not implimented yet
            # should return a sequence that is unique to the gogobot arduino program
        except:
            pass
        else:
            return serial
# ---------------------

def setup():
	# define classes and functions
	arduino = Arduino(_find_arduino())
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

