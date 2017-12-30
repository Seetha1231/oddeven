 def simp():
	(a,b,c)=map(int,sys.stdin.readline().split())
	print(int(a+(c-1)*b))
try:
	simp()
except:
	print('invalid')
