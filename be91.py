import sys
def cuboid():
	l,b,h=map(int,sys.stdin.readline().split())
	print(l*b*h)
try:
	cuboid()
except:
	print('invalid')
