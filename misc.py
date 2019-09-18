import numpy as np 
import time
import os
import sys
import random
import math
import matplotlib.pyplot as plt 
import timeit
import enum
from distances import *

'''
helper module for misc functions
'''

class CodeTimer:
    def __init__(self, name=None):
        self.name = f"'{name}'" if name else ''

    def __enter__(self):
        self.start = timeit.default_timer()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = round((timeit.default_timer() - self.start), 10) * 1000.0
        print(f"Code block {self.name} took: {str(self.took)} ms or {time_format(self.took/1000.0)}")

def removeDuplicates(arr):
	return list(dict.fromkeys(arr))

def truncate(x, level=100):
	'''truncate decimals off a number, the number of decimals left will be the same as the number of 0's on the level '''
	return int(x*level)/level

def percent(x, total=100, level=100):
	'''return a percentage of the total and truncate the number with the level '''
	return truncate((x/total)*100, level)

def time_format(secs):
	'''format the input number into hr:min:sec and return a string'''
	h = int(secs / (60 * 60))
	m = int((secs % (60 * 60)) / 60)
	s = secs % 60
	return ("%a : %a : %a" % (h, m, (s)))

def bar(x, char=None, Print=False):
	if Print:
		if char is None:
			print(x*"-")
		else:
			print(x*str(char))
	else:
		if char is None:
			return x*"-"
		else:
			return x*str(char)

def Map(val, valmin, valmax, outmin, outmax):
	return outmin + (outmax - outmin) * ((val - valmin) / (valmax - valmin))

def lerp(low, high, percent):
	return low + (high-low)*percent

def get_input(text):
	'''
	prints a [y/n] input with the inputed text and will return the boolean selection
	'''
	param = False
	while True:
		l = input(f'{text} [y/n]: ')
		param = False
		if l == 'y':
			param = True
			break
		elif l == 'n':
			break
		print("Invalid Input")
	return param

def Random(min, max=None):
	if type(min) is list:
		index = int(Random(len(min)))
		return min[index]
	elif max:
		return Map(random.random(), 0, 1, min, max)
	else:
		return Random(0, min)

def constrain(val, mini, maxi):
	return max(min(val, maxi), mini)

def factorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r

def fibbonaci(n):
	if n <= 1:
		return 0
	if n == 2 or n == 3:
		return 1

	return fibbonaci(n-1) + fibbonaci(n-2)

def Sqrt(x):
	return math.sqrt(x)

def abs(x):
	return Sqrt(pow(x, 2))

def sgn(x):
	return 0 if x == 0 else x/(abs(x))

def Xor(a, b):
	return ((a and not b) or (not a and b))

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (float(value) ** float(root_value), 3)

def now():
	return time.strftime("%I:%M:%S", time.localtime(time.time()))

def flat(x):
	if x.ndim == 1:
		return x
	if x.ndim != 2:
		raise Exception(f"array dimension must be 2")

	w, h = x.shape
	return x.reshape(w*h, 1)





if __name__ == "__main__":
	print(factorial(3000))




