def lcm2():
	(x,y)=map(int,sys.stdin.readline().split())
	temp=min(x,y)
	while(True):
		if temp%x==0 and temp%y==0:
			break
		temp+=1
	print(temp)
