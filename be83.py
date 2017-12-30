 def main():
	l=[]
	while(True):
		s=input()
		try:
			if '/' in s:
				a,b = map(int,s.split('/'))
				r=a/b
			else :
				a,b=map(int,s.split('%'))
				r=a%b
			l.append(int(r))
			r=[]
		except ValueError:
			break
	for i in l:
		print(i)
try:
	main()
except:
	print('invalid')
