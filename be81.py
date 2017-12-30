 import sys
 def getl():
	l=[]
	r=[]
	while(True):
		try:
			a,b = map(int,sys.stdin.readline().split())
		except ValueError:
			break
		l.append(a)
		l.append(b)
		r.append(l)
		l=[]
	for i in r:
		print(i[1]-i[0])
