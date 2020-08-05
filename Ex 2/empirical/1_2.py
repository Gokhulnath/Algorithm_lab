import time
import random

def max_subarray_sum_quadratic():
    total_time=0
    for i in range(10):
        start_time=time.time()
        a=[]
        for i in range(100):
           a.append(random.randint(-100,100))
        #print(a)
        #a=[1,2,3,4,5]
        n=len(a)
        prefix_sum=[0 for i in range(n)]
        for i in range(0,n):
            for j in range(0,i+1):
                prefix_sum[i]+=a[j]
        max=a[0]
        for i in range(0,n-1):
            for j in range(i,n):
                if (i==0 and j==n-1):
                    break;
                else:
                    sum=prefix_sum[j]-prefix_sum[i-1]
                    if(max<sum):
                        max=sum
        print("Maximum sum of subarray is = ",max)
        end_time=time.time()
        total_time+=end_time-start_time
    print("Total avergae runtime: ",total_time/10)

max_subarray_sum_quadratic()

'''
output:

=============== ARRAY OF SIZE 50 ===============
Maximum sum of subarray is =  648
Maximum sum of subarray is =  665
Maximum sum of subarray is =  363
Maximum sum of subarray is =  641
Maximum sum of subarray is =  576
Maximum sum of subarray is =  441
Maximum sum of subarray is =  867
Maximum sum of subarray is =  798
Maximum sum of subarray is =  545
Maximum sum of subarray is =  291
Total avergae runtime:  0.01336658000946045 
=============== ARRAY OF SIZE 100 ===============
Maximum sum of subarray is =  591
Maximum sum of subarray is =  512
Maximum sum of subarray is =  739
Maximum sum of subarray is =  773
Maximum sum of subarray is =  1035
Maximum sum of subarray is =  847
Maximum sum of subarray is =  818
Maximum sum of subarray is =  663
Maximum sum of subarray is =  429
Maximum sum of subarray is =  632
Total avergae runtime:  0.0173290491104126
=============== ARRAY OF SIZE 500 ===============
Maximum sum of subarray is =  1151
Maximum sum of subarray is =  1903
Maximum sum of subarray is =  1703
Maximum sum of subarray is =  1684
Maximum sum of subarray is =  1340
Maximum sum of subarray is =  1912
Maximum sum of subarray is =  2962
Maximum sum of subarray is =  1732
Maximum sum of subarray is =  953
Maximum sum of subarray is =  2248
Total avergae runtime:  0.1280665636062622
=============== ARRAY OF SIZE 1000 ===============
Maximum sum of subarray is =  2257
Maximum sum of subarray is =  1627
Maximum sum of subarray is =  2705
Maximum sum of subarray is =  2611
Maximum sum of subarray is =  2180
Maximum sum of subarray is =  2464
Maximum sum of subarray is =  2593
Maximum sum of subarray is =  1646
Maximum sum of subarray is =  2668
Maximum sum of subarray is =  3132
Total avergae runtime:  0.3867321252822876
'''
