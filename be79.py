import math
def persqr():
	n=int(input())
	m=int(input())
	m*=n
	s=math.sqrt(m)
	if s==int(s):
		print('yes')
	else :
		print('no')
try:
	persqr()
except:
	print('invalid')
