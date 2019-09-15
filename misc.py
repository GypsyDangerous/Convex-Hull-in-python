import numpy as np 
import time
import os
import sys
import random
import math
import matplotlib.pyplot as plt 
import timeit


'''
helper module for misc functions
'''


class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = timeit.default_timer()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (timeit.default_timer() - self.start) * 1000.0
        print('Code block' + self.name + ' took: ' + str(self.took) + ' ms')


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
	return ("%a: %a: %a" % (h, m, truncate(s)))

def array_percent(x, val):
	new = x.copy()
	for i in new:
		i = percent(i, val)
	return new

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

def tf(secs):
	return time.strftime("%M:%S", time.gmtime(secs))

def Map(val, valmin, valmax, outmin, outmax):
	return outmin + (outmax - outmin) * ((val - valmin) / (valmax - valmin))

def lerp(low, high, percent):
	return low + (high-low)*percent

def get_input(text):
	'''
	prints a [y/n] input with the inputted text and will return the boolean selection
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

def Random(mini, maxi=None):
	if type(mini) is list:
		index = int(Random(len(mini)))
		return mini[index]
	elif maxi:
		return Map(random.random(), 0, 1, mini, maxi)
	else:
		return Random(0, mini)

def ismultipleof(x, n):
	return x % n == 0


def constrain(val, mini, maxi):
	return max(min(val, maxi), mini)

def factorial(n):
    r = 1
    i = 2
    while i <= n:
        # Use shorter version
        r *= i
        i += 1
    return r

def fibbonaci(n):
	if n <= 1:
		return 0
	if n == 2 or n == 3:
		return 1

	return fibbonaci(n-1) + fibbonaci(n-2)

def BytestoMB(byte):
	return byte/1000000

def BytestoGB(byte):
	return BytestoMB(byte)/1000

def MBtoGB(mb):
	return mb/1000

def Sqrt(x):
	return math.sqrt(x)

def Abs(x):
	return math.sqrt(pow(x, 2))

def abs(x):
	return Abs(x)

def sgn(x):
	if x == 0:
		return 0
	return x/(Abs(x))

def Xor(a, b):
	return ((a and not b) or (not a and b))

def dist(arr1, arr2=None):
	arr1 = np.array(arr1).flatten()
	if arr2 is None:
		return mag(arr1)
	arr2 = np.array(arr2).flatten()
	

	if len(arr1) != len(arr2):
		raise Exception("vector lengths don't match")

	return mag(arr1-arr2)

def mag(vec):
	return Sqrt(np.sum(vec**2))

def manhattan_dist(arr1, arr2):
	return sum(abs(a-b) for a,b in zip(arr1,arr2))

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (float(value) ** float(root_value), 3)

def minkowski_distance(x,y,p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

def string_to_num1(string, maxlen=0):
	string = string.lower()
	result = [constrain(ord(i)-96, 0, 27) for i in string]
	while len(result) < maxlen:
		result.append(0)
	return result

def string_to_num2(string, maxlen=0):
	result = [ord(i) for i in string]
	while len(result) < maxlen:
		result.append(0)
	return np.array(result)/127

def now():
	return time.strftime("%I:%M:%S", time.localtime(time.time()))

def flat(x):
	if x.ndim == 1:
		return x
	if x.ndim != 2:
		raise Exception(f"array dimension must be 2")

	w, h = x.shape
	return x.reshape(w*h, 1)

def progress(count, total, status=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))

	percents = round(100.0 * count / float(total), 1)
	if count < total:
		bar = '=' * (filled_len) + '>' + '-' * (bar_len - filled_len-1)
	else:
		bar = '=' * (filled_len) + '-' * (bar_len - filled_len)

	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
	sys.stdout.flush()





if __name__ == "__main__":
	print(abs(-100))




