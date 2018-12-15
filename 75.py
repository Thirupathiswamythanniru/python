num=input("")
b=len(num)
s=list(num)
l=[]
if b%2!=0:
  for i in range(b//2):
    l+=s[i]
  l+='*'
  j=b//2+1
else:
  for i in range(b//2-1):
    l+=s[i]   
  l+='**'
  j=b//2+1
for i in range(j,b):
  l+=s[i]
print(''.join(l),end='')  
