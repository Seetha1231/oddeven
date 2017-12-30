def composites():
	n=int(input())
	l=[]
	f=0
	for i in range(1,n//2+1):
		if n%i==0:
			l.append(i)
	l.append(n)
	for i in l:
		print(i)
