def Merge(a,b):

    if a==[]:
        return b
    if b==[]:
        return a
    if a[0]<b[0]:
        return [a[0]]+Merge(a[1:],b)
    else:
        return [b[0]]+Merge(a,b[1:])


def MergeSort(a):
    if a==[]:
        return 0
    if len(a)==1:
        return a
    m=int(len(a)/2)
    return Merge(MergeSort(a[:m]),MergeSort(a[m:]))

v=[]
n=int(input("Please enter the number of elements in the list: "))
for i in range(n):
    x=int(input("Please enter the number: "))
    v.append(x)
print(MergeSort(v))
