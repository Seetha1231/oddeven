 def simp():
	(a,b,c)=map(int,sys.stdin.readline().split())
	print(int((a*b)/c))
try:
	simp()
except:
	print('invalid')
