 def firstk():
	str=input()
	s=''
	k=int(input())
	for i in range(0,k):
		s+=str[i]
	print(s)
try:
	firstk()
except:
	print('invalid')
