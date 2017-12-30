def main():
	min=999
	l=[int(input()) for i in range(10)]
	for i in range(10):
		if min>l[i]:
			min=l[i]
	print(min)
