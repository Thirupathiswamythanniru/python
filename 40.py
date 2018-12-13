def f(num):
 if(num<=1):
  return (num)
 else:
  return(f(num-1)+f(num-2))
num=int(input(''))
for i in range(1,num+1):
  if(i<num):
   print(f(i),end=' ')
  else:
   print(f(i),end='')
