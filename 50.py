f=0
n=int(input())
if(n==1):
  print(('yes'),end='')
else:
  while(n!=0):
    n=n/2
    if n==1:
      f=1
      break
  if f!=1:
    print(('no'),end='')
  else:
    print(('yes'),end='') 
