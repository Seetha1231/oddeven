def proddig():
	n=int(input())
	p=1
	while(n!=0):
		r=n%10
		p=p*r
		n//=10
	print(p)
try:
	proddig()
except:
	print('invalid')
