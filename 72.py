n=input("")
vo=set('aeiou')
if not vo.isdisjoint(n):
    print (("yes"),end='')
else:
    print (("no"),end='')
