import sys
def gcd2():
	(x,y)=map(int,sys.stdin.readline().split())
	while(y!=0):
		t=y
		y=x%y
		x=t
	print(x)
try:
	gcd2()
except:
	print('invalid')
