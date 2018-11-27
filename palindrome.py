n=int(input())
temp=n
rev=0
if(n<=1000):
  while(temp!=0):
	  rem=temp%10
	  rev=rev*10+rem
	  temp=int(temp/10)
  if rev==n:
	  print('yes')
  else :
	  print('no')
