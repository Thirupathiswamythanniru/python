s,e=map(int,input().split())
for i in range(s+1,e):
  if i%2==0 :
    if(i<e):
	    print(i,end=' ')
    else:
      print(i,end="")
