def lengthes(j):
    var=0
    for i in range(0,j):
        if(a[i]<a[j]):
            var=max(best,lengthes(i))
    return (var+1)
def list(a,i,j):
    a.insert(j,float('inf'))
    return lengthes(j)-1

a=[5,2,8,6,3,6,9,7]
print(list(a,0,8))
    
