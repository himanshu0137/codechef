from math import *
from sys import stdin,stdout
def cross(v1, v2):
    #return the cross product of two vectors 
    return (v1[0] * v2[1]) - (v1[1] * v2[0])

def angle_cmp(pivot):
    ''' receive a coord as the pivot and return a 
    function for comparing angles formed by another
    two coords around the pivot
    '''
    def _angle_cmp(c1, c2):
        v1 = c1[0] - pivot[0], c1[1] - pivot[1]
        v2 = c2[0] - pivot[0], c2[1] - pivot[1]
        cp = cross(v1, v2)
        if cp < 0:
            return 1
        elif cp == 0:
            return 0
        else:
            return -1
    return _angle_cmp

def turnning(c1, c2, c3):
    #detemine which way does c1 -> c2 -> c3 go
    v1 = c2[0] - c1[0], c2[1] - c1[1]
    v2 = c3[0] - c2[0], c3[1] - c2[1]
    cp = cross(v1, v2)
    if cp < 0:
        return 'RIGHT'
    elif cp == 0:
        return 'STRAIGHT'
    else:
        return 'LEFT'
    
def graham_scan(coords):
    num = len(coords)
    if num < 3:
        raise Exception('too few coords') 
    coords.sort()

    # select the leftmost coord as the pivot
    pivot = coords[0] 
    coords = coords[1:]

    # for remaining coords, sort them by polar angle
    # in counterclockwise order around pivot
    coords.sort(angle_cmp(pivot)) 
    
    # push the first three coords in a stack
    stack = []
    stack.append(pivot)
    stack.append(coords[0])
    stack.append(coords[1])
    
    # for the rest of the coords, while the angle formed by 
    # the coord of the next-to-top of the stack, coord of 
    # top of stack and the next coord makes a nonleft turn, 
    # pop the stack
    # also, push the next coord into the stack at each loop
    for i in range(2, num - 1):
        while len(stack) >= 2 and \
              turnning(stack[-2], stack[-1], coords[i]) != 'LEFT':
            stack = stack[:-1]
        stack.append(coords[i])
    return stack
t = int(stdin.readline())
for _ in xrange(t):
	n = int(stdin.readline())
	a = map(int,stdin.readline().split())
	point = []
	for i in xrange(len(a)-1):
		for j in xrange(i+1,len(a)):
			point.append((a[i],a[j]))
	ch = graham_scan(point)
	area = 0
	for i in xrange(len(ch)):
		area += ch[i][0]*ch[(i+1)%len(ch)][1]-ch[i][1]*ch[(i+1)%len(ch)][0]
	stdout.write(str(abs(area))+"\n")