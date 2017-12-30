def si():
	(p,n,r)=map(int,sys.stdin.readline().split())
	sii=p*n*r/100
	print(math.floor(sii))
try:
	si()
except:
	print('invalid')
