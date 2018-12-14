s=input()
if all(i in '01' for a in s):
    print (("yes"),end='')
else:
    print (("No"),end='')
if not(s.translate(None,'01')):
    print (("yes"),end='')
else:
    print (("No"),end='')
