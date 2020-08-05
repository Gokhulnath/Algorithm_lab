from time import process_time
import random
import math as math
def exhaustive_inversions(i):
    ans=0
    for j in range(0,len(i)):
        for k in range(j+1,len(i)):
            if(i[j]>i[k]):
                ans=ans+1
    return(ans)



a1=[1,2,3,4,5]
a2=[2,4,1,3,5]
a3=[3,1,2,5,4]
a4=[4,5,2,1,3]
a5=[5,4,3,2,1]


print("\n\nEmpirical Analysis")
print("\nBrute Force")
for i in [10,50,100,1000,5000,10000]:
	a=[x for x in range(i,0,-1)]
	t1_start=process_time()
	exhaustive_inversions(a)
	t1_stop=process_time()
	print ("Size:",i,"Time:",t1_stop-t1_start,"Ratio:",(t1_stop-t1_start)/(i**2))

'''
[0, [1, 2, 3, 4, 5]]
[3, [1, 2, 3, 4, 5]]
[3, [1, 2, 3, 4, 5]]
[7, [1, 2, 3, 4, 5]]
[10, [1, 2, 3, 4, 5]]


Empirical Analysis

Brute Force
Size: 10 Time: 0.0 Ratio: 0.0
Size: 50 Time: 0.0 Ratio: 0.0
Size: 100 Time: 0.0 Ratio: 0.0
Size: 1000 Time: 0.03125 Ratio: 3.125e-08
Size: 5000 Time: 0.90625 Ratio: 3.625e-08
Size: 10000 Time: 3.59375 Ratio: 3.59375e-08

'''
