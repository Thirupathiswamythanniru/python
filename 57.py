m,n=map(int,input().split())
list=[int(x) for x in input().split()]
if n in list:
    count=list.count(n)
    print (count)
else:
    print ((0),end='')
