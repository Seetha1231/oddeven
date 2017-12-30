def kthno():
	l=[]
	(n,k)=map(int,sys.stdin.readline().split())
	for i in range(n):
		l.append(int(input()))
	print(l[k-1])
try:
	kthno()
except:
	print('invalid')
