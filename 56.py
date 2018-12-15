def main():
	try:
		c=0
		m=0
		n=input()
		for i in n:
			if i.isalpha():
				c=c+1
			elif i.isnumeric():
				m=m+1
		if c+m==len(n) and c>0 and m>0:
			print('yes')
		else :
			print('no')
	except:
		print('invalid')
main()
