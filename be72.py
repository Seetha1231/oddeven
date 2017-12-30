def hasvowel():
	v=['a','e','i','o','u','A','E','I','O','U']
	st=input()
	for i in st:
		if i in v:
			return 'yes'
	return 'no'
try:
    hasvowel()
except:
    print('invalid')
