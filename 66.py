num = int(input(""))
for i in range(2,int(num)):
    if (num%i==0):
      print(("no"),end='')
      break
else:
    print(("yes"),end='')
