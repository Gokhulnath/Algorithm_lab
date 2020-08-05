from time import process_time
import random
import math as math


def merge(a,b):
    inv=0
    i=0
    j=0
    c=[]
    while(i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            c.append(a[i])
            i=i+1
        elif(b[j]<a[i]):
            c.append(b[j])
            j=j+1
            inv+=(len(a)-i)
    if(i<len(a)):
        c=c+a[i:]
    if(j<len(b)):
        c=c+b[j:]
    t=[inv,c]
    return(t)

def improvised_inversions(a):
    inv=0
    if(len(a)>1):
        mid=len(a)//2
        t1=improvised_inversions(a[:mid])
        t2=improvised_inversions(a[mid:])
        t3=merge(t1[1],t2[1])
        a=t3[1]
        inv=(t1[0]+t2[0]+t3[0])
    t=[inv,a]
    return(t)




a1=[1,2,3,4,5]
a2=[2,4,1,3,5]
a3=[3,1,2,5,4]
a4=[4,5,2,1,3]
a5=[5,4,3,2,1]
for i in [a1,a2,a3,a4,a5]:
  ans=improvised_inversions(i)
  print(ans)


print("\nImprovised")
for i in [10,50,100,1000,5000,10000,50000,100000]:
	a=[x for x in range(i,0,-1)]
	t1_start=process_time()
	improvised_inversions(a)
	t1_stop=process_time()
	print ("Size:",i,"Time:",t1_stop-t1_start,"Ratio:",((t1_stop-t1_start)/(i*math.log(i,2))))



'''
[0, [1, 2, 3, 4, 5]]
[3, [1, 2, 3, 4, 5]]
[3, [1, 2, 3, 4, 5]]
[7, [1, 2, 3, 4, 5]]
[10, [1, 2, 3, 4, 5]]

Improvised
Size: 10 Time: 0.0 Ratio: 0.0
Size: 50 Time: 0.0 Ratio: 0.0
Size: 100 Time: 0.0 Ratio: 0.0
Size: 1000 Time: 0.015625 Ratio: 1.567864560749902e-06
Size: 5000 Time: 0.03125 Ratio: 5.086382075806015e-07
Size: 10000 Time: 0.078125 Ratio: 5.879492102812133e-07
Size: 50000 Time: 0.390625 Ratio: 5.004919884474067e-07
Size: 100000 Time: 0.765625 Ratio: 4.609521808604712e-07
'''
