from pyvector import *



def findSide(p1, p2, p):
	'''
	returns which side points 'p' is from the line segment p1->p2

	parameters
		start - the first point that defines line segment start->end
		end - the second point that defines line segment start->end
		points - list of points to compare against the line segment

	returns
		integer, either 1, 0, or -1 based on the side the point is of the line
	'''
	ab = p1-p2
	ap = p1-p
	return sgn(ab.cross(ap).z)

def isCCW(a, b, p):
	'''
	wrapper function for findSide() function to determine if it returns a certain value

	parameters
		start - the first point that defines line segment start->end
		end - the second point that defines line segment start->end
		points - list of points to compare against the line segment

	returns
		boolean
	'''
	return findSide(a, b, p) == -1


def get_points_left_of_line(start, end, points):
	'''
	Returns all points that are LEFT of a line start->end

	parameters
		start - the first point that defines line segment start->end
		end - the second point that defines line segment start->end
		points - list of points to compare against the line segment

	returns
		list
	'''
	return [pt for pt in points if isCCW(start, end, pt)]


def farthest_point_from_line(start, end, points):
	'''
	Returns the farthest point from line segment start->end from a list of points

	parameters
		start - the first point that defines line segment start->end
		end - the second point that defines line segment start->end
		points - list of points to compare against the line segment

	returns 
		PyVector
	'''
	max_dist = 0
	max_point = None

	for point in points:
		if point != start and point != end:
			dist = pointLineDist(start, end, point)
			if dist > max_dist:
				max_dist = dist
				max_point = point

	return max_point

def minMaxPoints(points):
	'''
	returns two points, the point in the list of points that has the smallest x value and the point in the list with the largest x value

	parameters
		list of points (PyVector) to get the min and max X from

	returns
		tuple of min and max points
	'''
	p = points.copy()
	p.sort(key=lambda a: a.x)
	return p[0], p[-1]


def pointLineDist(start, end, pt):
	'''
	returns the shortest distance from a point 'pt' to a line segment start->end

	parameters
		start - the first point that defines line segment start->end
		end - the second point that defines line segment start->end
		pt - point being compared with the line segment

	returns
		integer, distance from point to line
	'''
	ap = pt - start
	ab = (end - start).normalize()
	d = ap.dot(ab)
	ab *= d
	n = start + ab
	return pt.dist(n)


class convexHull():
	'''
	class containing many convex hull algorithms with functionality to display the hull
	'''
	def __init__(self):
		self.hull = [];

	def __str__(self):
		return '\n'.join([str(p) for p in self.hull])


	def getquickhull(self, points):
		'''
		Wrapper function for the recursive quickhull() function that returns the convex hull
		surrounding a set of points using the quickhull algorithm 

		parameters
			points - the list of points to create a convex hull for

		returns
			list, the hull around the points
		'''
		self.most_recent_points = points.copy()

		min, max = minMaxPoints(points)
		
		self.hull = self.quickhull(points, min, max) + self.quickhull(points, max, min)
		
		return self.hull
	
	def quickhull(self, listPts, min, max):
		'''
		function to calculate the convex hull around a set of points.
		uses the recursive quickhull algorithm

		parameters
			listPts - list of points operate on
			min - starting point of the line segment that divides the points in listPts
			max - end point of the line segment that divides the points in listPts

		returns
			list, part of convexhull
		'''

		left_of_line_pts = get_points_left_of_line(min, max, listPts)
		
		ptC = farthest_point_from_line(min, max, left_of_line_pts)
		
		if (ptC) == None:
		    return [max]
		
		hullPts = self.quickhull(left_of_line_pts, min, ptC)
		
		hullPts = hullPts + self.quickhull(left_of_line_pts, ptC, max)
		
		return hullPts

	@property
	def hull_length(self):
		'''
		return the length of the current hull
		'''
		return len(self.hull)



	@property
	def loop_hull(self):
		'''
		return the current hull with the first value added to end to allow drawing a closed loop
		does not affect the hull 
		'''
		return self.hull+[self.hull[0]]
	

	def show(self):
		'''
		display the hull and the points it surrounds using matplotlib

		blue points - points in full list of points
		red points - points in the convex hull
		blue line - line connecting the convex hull
		'''
		x1 = [p.x for p in self.loop_hull]
		y1 = [p.y for p in self.loop_hull]
		x2 = [p.x for p in self.most_recent_points]
		y2 = [p.y for p in self.most_recent_points]
		plt.title(f"Convex hull with {self.hull_length} points")
		plt.plot(x2,y2, 'bo')
		plt.plot(x1,y1)
		plt.plot(x1,y1, 'ro')
		plt.show()



def main():
	n = 3000
	k = 2000
	sizes = 20
	Convex = convexHull()

	with CodeTimer(f"generating {n} points"):
		points = []
		for i in range(sizes):
			mean = Random(-k*10, k*10)
			mean2 = Random(-k*10, k*10)
			points = points+[PyVector(np.random.normal(mean, k, (1,))[0], np.random.normal(mean2, k, (1,))[0]) for i in range(n//sizes)]
		# points = [PyVector.random2D()*k for i in range(n)]
	with CodeTimer(f"QuickHull with {n} points"):
		hull = Convex.getquickhull(points)
	
	print(f"{len(Convex.hull)} points in the hull")
	
	
	graph = True

	if graph:
		Convex.show()

if __name__ == "__main__":
	main()

