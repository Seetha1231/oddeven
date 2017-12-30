def lastk():
	s=input()
	k=int(input())
	d=len(s)-k
	print(s[d:])
try:
	lastk()
except:
	print('invalid')
