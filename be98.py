def changed():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	for i in range(1,n):
		if l[i-1]>l[i]:
			print(l[i-1])
			break
try:
	changed()
except:
	print('invalid')
