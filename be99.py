import sys
def stat():
	(a,b,c)=map(int,sys.stdin.readline().split())
	print((a*b)%c)
try:
	stat()
except:
	print('invalid')
