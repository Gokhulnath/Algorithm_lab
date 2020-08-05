def fast_power(x,n):
    if n==0:
        return 1
    if (n%2)!=0:
        return x*fast_power(x,n-1)
    else:
        return fast_power(x,n/2)*fast_power(x,n/2)


x=int(input("Please enter the number: "))
n=int(input("Please enter the exponent: "))
print(fast_power(x,n))
