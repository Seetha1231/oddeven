def between():
	n=int(input())
	s=int(input())
	e=int(input())
	for i in range(s,e):
		if i==n:
			return 'yes'
	return 'no'
try:
	between()
except:
	print('invalid')
  
