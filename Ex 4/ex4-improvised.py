

def partition(a,pivot):
    s=0
    e=len(a)-2
    while(s<e):
        if(a[s]>pivot and a[e]<pivot):
            (a[s],a[e])=(a[e],a[s])
            s=s+1
            e=e-1
        if(a[s]<pivot):
            s=s+1
        if(a[e]>pivot):
            e=e-1
    if(a[e]>pivot):
        (a[len(a)-1],a[e])=(a[e],a[len(a)-1])
        return e
    else:
        (a[len(a)-1],a[e+1])=(a[e+1],a[len(a)-1])
        return e+1


def move_pivot(a,pivot):
    for i in range(0,len(a)):
        if(a[i]==pivot):
            a=a[:i]+a[i+1:]+[a[i]]
            return a

def improvised_nuts_bolts(nuts,bolts):
    if(len(nuts)==1 or len(nuts)==0):
        return [nuts,bolts]
    nuts=move_pivot(nuts,bolts[len(bolts)-1])
    a=partition(nuts,bolts[len(bolts)-1])
    bolts=move_pivot(bolts,nuts[a])
    a=partition(bolts,nuts[a])
    c=improvised_nuts_bolts(nuts[:a],bolts[:a])
    d=improvised_nuts_bolts(nuts[a+1:],bolts[a+1:])
    return [c[0]+[nuts[a]]+d[0],c[1]+[bolts[a]]+d[1]]


a=[11,5,2,7,9,3]
b=[3,2,11,7,9,5]
c=improvised_nuts_bolts(a,b)
print("Matched nuts and bolts")
print(c)


'''
Matched nuts and bolts
[[2, 3, 5, 7, 9, 11], [2, 3, 5, 7, 9, 11]]
'''
