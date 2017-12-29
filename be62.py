def checkbin():
	l=['0','1']
	f=0
	st=input()
	for i in range(len(st)):
		if st[i] in l:
			continue
		else :
			f=1
			break
	if f!=1:
		print('yes')
	else :
		print('no')
