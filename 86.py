s=input()
l=list(s)
r=[]
for i in l:
	if not i in r:
	  r.append(i)
if len(l)==len(r):
	print('Yes',end='')
else :
	print('No',end='')
