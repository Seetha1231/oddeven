try:
	n=int(input())
	for i in range(n):
		p=2**i
		if p>n:
			print(p)
			break
except:
	print('invalid')
