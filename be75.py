 def midchenge():
	s=input()
	n=len(s)
	l=list(s)
	s=''
	if n%2!=0:
		for i in range(n//2):
			s+=l[i]
		s+='*'
		j=n//2+1
	else:
		for i in range(n//2-1):
			s+=l[i]
		s+='**'
		j=n//2+1
	for i in range(j,n):
		s+=l[i]
	print(s)
try:
	midchenge()
except:
	print('invalid')
