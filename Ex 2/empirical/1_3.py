import time
import random


def max_subaay_sum_linearithmic(a, l, m, h) : 
    sm = 0; left_sum = -10000
    for i in range(m, l-1, -1) : 
        sm = sm + a[i] 
        if (sm > left_sum) : 
            left_sum = sm 
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + a[i]  
        if (sm > right_sum) : 
            right_sum = sm 
    return left_sum + right_sum; 
  

def maxSubaaySum(a, l, h) : 
    if (l == h) : 
        return a[l] 
    m = (l + h) // 2
    return max(maxSubaaySum(a, l, m), 
               maxSubaaySum(a, m+1, h), 
               max_subaay_sum_linearithmic(a, l, m, h)) 
              
total_time=0
for i in range(10):
    start_time=time.time()
    a=[]
    for i in range(100):
       a.append(random.randint(-100,100))  
    n = len(a) 
  
    max_sum = maxSubaaySum(a, 0, n-1) 
    print("Maximum contiguous sum is ", max_sum)
    end_time=time.time()
    total_time+=end_time-start_time
print("Total avergae runtime: ",total_time/10)
  
'''
output:
=============== ARRAY OF SIZE 50 ===============
Maximum contiguous sum is  429
Maximum contiguous sum is  428
Maximum contiguous sum is  241
Maximum contiguous sum is  175
Maximum contiguous sum is  326
Maximum contiguous sum is  261
Maximum contiguous sum is  474
Maximum contiguous sum is  1038
Maximum contiguous sum is  381
Maximum contiguous sum is  303
Total avergae runtime:  0.01405494213104248
>>> 
=============== ARRAY OF SIZE 100 ===============
Maximum contiguous sum is  901
Maximum contiguous sum is  1000
Maximum contiguous sum is  1148
Maximum contiguous sum is  352
Maximum contiguous sum is  971
Maximum contiguous sum is  320
Maximum contiguous sum is  418
Maximum contiguous sum is  338
Maximum contiguous sum is  1238
Maximum contiguous sum is  964
Total avergae runtime:  0.012237811088562011
>>> 
=============== ARRAY OF SIZE 500 ===============
Maximum contiguous sum is  790
Maximum contiguous sum is  1791
Maximum contiguous sum is  769
Maximum contiguous sum is  1213
Maximum contiguous sum is  1196
Maximum contiguous sum is  1828
Maximum contiguous sum is  1889
Maximum contiguous sum is  738
Maximum contiguous sum is  1924
Maximum contiguous sum is  2637
Total avergae runtime:  0.014631009101867676
>>> 
=============== ARRAY OF SIZE 1000 ===============
Maximum contiguous sum is  1650
Maximum contiguous sum is  2082
Maximum contiguous sum is  3295
Maximum contiguous sum is  1337
Maximum contiguous sum is  4380
Maximum contiguous sum is  1714
Maximum contiguous sum is  1818
Maximum contiguous sum is  2154
Maximum contiguous sum is  1589
Maximum contiguous sum is  3904
Total avergae runtime:  0.019869780540466307
'''
