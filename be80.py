 def odddig():
	n=int(input())
	r=[]
	while(n!=0):
		r.append(n%10)
		n//=10
	for i in range(len(r)-1,-1,-1):
		if r[i]%2!=0:
			print(r[i])
try:
	odddig()
except:
	print('invalid')
