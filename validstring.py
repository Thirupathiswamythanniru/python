n =input(' ')
try:
 n=float(n)
 n=int(n)
 if(n%1==0):
   print('yes')
except:
  print('no',end='')
  
