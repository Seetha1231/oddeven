def isogram():
	s=input()
	l=list(s)
	r=[]
	for i in l:
		if not i in r:
			r.append(i)
	if len(l)==len(r):
		print('yes')
	else :
		print('no')
try:
	isogram()
except:
	print('invalid')
