n = int(input(" "))
exp = int(input(" "))
power = 1
for i in range(1, exp + 1):
    power = power * n   
print("The Result of {0} Power {1} = {2}".format(n, exp, power))
