num=int(input(""))
count=0
if num>1:
    for i in range(2,num):
        if num%i==0:
            count=count+1
if count>1:
    print (("yes"),end='')
else:
    print (("no"),end='')
