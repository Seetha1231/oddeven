def countsen():
	sen=input()
	print(sen)
	c=1
	for i in range(len(sen)):
		if sen[i]==' ':
			c+=1
	print(c)
try:
	countsen()
except:
	print('invalid') 
