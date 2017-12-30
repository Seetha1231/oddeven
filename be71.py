def pali():
	str1=input()
	str2=str1[::-1]
	if str1==str2:
		print('yes')
	else :
		print('no')
try:
	pali()
except:
	print('invalid')
