import math
k,l=map(int,input().split())
a=k * l
if math.sqrt(a).is_integer():
    print (("yes"),end='')
else:
    print (("no"),end='')
