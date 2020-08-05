x=int(input("Please enter the number: "))
n=int(input("Please enter the exponent: "))
power=1

for i in range(int(n/2)):
    power*=x

if((n%2)!=0):
    print(x*power*power)
else:
    print(power*power)
