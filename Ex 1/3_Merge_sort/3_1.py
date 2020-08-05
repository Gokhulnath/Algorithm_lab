def ordered_insert(u,v):
    if(v==[]):
        return [u]+v
    if(u < v[0]):
        return [u]+v
    else:
        return [v[0]]+ordered_insert(u,v[1:])



def ordered_merge(a,b):
    if(a==[]):
        return b
    if(b==[]):
        return a
    return ordered_merge(ordered_insert(b[0],a),b[1:])




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
print(ordered_merge(u,v))
