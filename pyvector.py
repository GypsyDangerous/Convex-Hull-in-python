import numpy as np 
import random
import math
from misc import *

class PyVector:

	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y 
		self.z = z

	def __add__(self, n):
		temp = self.copy();
		temp.x+=n.x
		temp.y+=n.y
		temp.z+=n.z
		return temp


	def __sub__(self, vector):
		temp = self.copy();
		temp.x -= vector.x
		temp.y -= vector.y
		temp.z -= vector.z
		return temp

	def __truediv__(self, divisor):
		temp = self.copy();
		temp.x /= divisor
		temp.y /= divisor
		temp.z /= divisor
		return temp

	def __mul__(self, multer):
		temp = self.copy();
		if isinstance(multer, PyVector):
			temp.x *= multer.x
			temp.y *= multer.y
			temp.z *= multer.z
		else:
			temp.x *= multer
			temp.y *= multer
			temp.z *= multer
		return temp

	def __iter__(self):
		return iter([self.x, self.y, self.z])

	def __str__(self):
		return f"({self.x},{self.y})"

	def set(self, x, y=0, z=0):
		if isinstance(x, PyVector):
			self.set(x.x, x.y, x.z)
		else:
			self.x = x
			self.y = y
			self.z = z

	def heading(self):
		return math.atan2(self.y, self.x)

	def setHeading(self, heading):
		mag = self.mag()
		self.set(PyVector.fromAngle(heading))
		self.setMag(mag)

	def mag(self):
		return round(math.sqrt(self.magSq()), 30);

	def magSq(self):
		return (self.x**2 + self.y**2 + self.z**2)

	def setMag(self, Mag):
		self.normalize()
		temp = self.copy()
		temp *= Mag
		self.set(temp)
		return self

	def normalize(self):
		temp = self.copy()
		temp /= (temp.mag())
		self.set(temp)
		return self

	def dist(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		dz = self.z - other.z
		return math.sqrt(dx*dx + dy*dy + dz*dz);

	def distSQ(self, other):
		return self.dist(other)**2

	def rotate(self, theta):
		temp = self.x
		self.x = (self.x*math.cos(theta)) - (self.y*math.sin(theta))
		self.y = (temp*math.sin(theta)) + (self.y*math.cos(theta))
		
	def copy(self):
		return PyVector(self.x, self.y, self.z)

	def dot(self, other):
		return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

	@classmethod
	def Polar(cls, r, theta):
		return cls.fromAngle(theta).setMag(r)

	@classmethod
	def angleBetween(cls, a, b):
		return math.acos(a.dot(b)/(a.mag()*b.mag()))

	@classmethod
	def random2D(cls):
		r = cls(Random(-1, 1), Random(-1, 1))
		r.normalize()
		return r

	@classmethod
	def random3D(cls):
		r = cls(Random(-1, 1), Random(-1, 1), Random(-1, 1))
		r.normalize()
		return r

	@classmethod
	def fromAngle(cls, theta):
		x = math.cos(theta)
		y = math.sin(theta)
		return cls(x, y).normalize()

if __name__ == "__main__":
	a = PyVector.random2D() 
	a *= 10
	print(a.mag(), a.heading())
	a.setHeading(math.pi/2)
	print(a.mag(), a.heading())