def Lengthdp(a,n):
    b.insert(n,float('inf'))
    len=[]
    for j in range(0,n+1):
        len.insert(j,0)
        for i in range(0,j):
            if(a[i]<a[j]):
                len[j]=max(len[j],len[i])
        len[j]=len[j]+1
    return (len[n]-1)

b=[5,2,8,6,3,6,9,7]
print(Lengthdp(a,8))
    
