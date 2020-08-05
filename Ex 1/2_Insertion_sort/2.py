def ordered_insert(u,v):
    if(v==[]):
        return [u]+v
    if(u < v[0]):
        return [u]+v
    else:
        return [v[0]]+ordered_insert(u,v[1:])

v=[]
n=int(input("Please enter the number of elements in the list: "))
for i in range(n):
    x=int(input("Please enter the number: "))
    v.append(x)
u=int(input("Please enter the number to insert in the ordered list: "))
print(ordered_insert(u,v))
