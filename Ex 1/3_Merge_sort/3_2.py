def Merge(a,b):

    if a==[]:
        return b
    if b==[]:
        return a
    if a[0]<b[0]:
        return [a[0]]+Merge(a[1:],b)
    else:
        return [b[0]]+Merge(a,b[1:])

u=[]
n=int(input("Please enter the number of elements in the 1st list: "))
for i in range(n):
    x=int(input("Please enter the number: "))
    u.append(x)
v=[]
n=int(input("Please enter the number of elements in the 2nd list: "))
for i in range(n):
    x=int(input("Please enter the number: "))
    v.append(x)
print(Merge(u,v))
