from pyvector import *
from functools import reduce
import matplotlib.pyplot as plt


def removeDuplicates(arr):
	return list(dict.fromkeys(arr))

def findSide(p1, p2, p):
	val = (p.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p.x - p1.x); 
  
	if (val > 0):
		return 1; 
	if (val < 0):
		return -1; 
	return 0; 


def getquickhull(points, hull=[]):
	# get the min, and max from the list of points
    min, max = minMaxPoints(points)

    hullpts = quickhull(points, min, max)

    hullpts = hullpts + quickhull(points, max, min)

    return hullpts

def quickhull(listPts, min, max):
    left_of_line_pts = get_points_left_of_line(min, max, listPts)

    ptC = maxPointLineDist(min, max, left_of_line_pts)

    if (ptC) == None:
        return [max]

    hullPts = quickhull(left_of_line_pts, min, ptC)

    hullPts = hullPts + quickhull(left_of_line_pts, ptC, max)

    return hullPts


def isCCW(a, b, p):
	return findSide(a, b, p) == 1

'''
    Reterns all points that a LEFT of a line start->end
'''
def get_points_left_of_line(start, end, points):
    pts = []

    for pt in points:
        if isCCW(start, end, pt):
            pts.append(pt)

    return pts

'''
    Returns the maximum point from a line start->end
'''
def maxPointLineDist(start, end, points):
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
    p = points.copy()
    p.sort(key=lambda a: a.x)
    return p[0], p[-1]


def pointLineDist(start, end, pt): # pt is the point
    x1, y1, _ = start
    x2, y2, _ = end
    x0, y0, _ = pt
    nom = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denom = ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5
    result = nom / denom
    return result

if __name__ == "__main__":
	n = 30000
	points = [PyVector(Random(2000), Random(2000)) for i in range(n)]
	with CodeTimer(f"QuickHull with {n} points"):
		hull = getquickhull(points)
	
	print(f"{len(hull)} points in the hull")
	
	
	graph = True #get_input("graph points?")
	
	
	if graph:
		x = [p.x for p in points]
		y = [p.y for p in points]
		x1 = [p.x for p in hull]
		y1 = [p.y for p in hull]
		
		plt.plot(x,y, 'bo')
		plt.plot(x1,y1)
		plt.show()

