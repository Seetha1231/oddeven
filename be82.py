def farmarea():
	l,b=map(float,sys.stdin.readline().split())
	a=l*b
	print(round(a,5))
try:
	farmarea()
except:
	print('invalid')
