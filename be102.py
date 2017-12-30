def main():
	n=int(input())
	while(True):
		if n%2==0:
			n//=2
		else :
			print(n)
			break
try:
	main()
except:
	print('invalid')
