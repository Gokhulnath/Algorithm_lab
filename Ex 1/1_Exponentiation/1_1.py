def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

x=int(input("Please enter the number: "))
n=int(input("Please enter the exponent: "))

print(power(x,n))
