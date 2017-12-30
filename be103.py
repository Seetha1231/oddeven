def main():
	s=input()
	l=s.split()
	st=''
	for i in l:
		st+=i.title()+' '
	print(st)
