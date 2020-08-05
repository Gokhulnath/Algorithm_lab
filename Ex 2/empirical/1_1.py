import time
import random

def sum(a,i,j):
    if(i==j):
        return 0
    else:
        return a[i]+sum(a,i+1,j)

total_time=0
for i in range(10):
    start_time=time.time()
    a=[]
    for i in range(100):
       a.append(random.randint(-100,100))
    #print(a)
    #a=[1,2,3,4,5]
    n=len(a)
    b=[[0 for i in range(n)] for i in range(n-1)]

    for i in range(0,n-1):
        for j in range(i,n):
            if (i==0 and j==n-1):
                break;
            else:
                if (i!=j):
                    b[i][j]=sum(a,i,j+1)
    print("Maximum sum of subarray is = ",max(max(x) for x in b))

    end_time=time.time()
    total_time+=end_time-start_time
print("Total avergae runtime: ",total_time/10)


'''
Output:

=============== ARRAY OF SIZE 50 ===============
Maximum sum of subarray is =  162
Maximum sum of subarray is =  258
Maximum sum of subarray is =  203
Maximum sum of subarray is =  294
Maximum sum of subarray is =  780
Maximum sum of subarray is =  639
Maximum sum of subarray is =  413
Maximum sum of subarray is =  153
Maximum sum of subarray is =  292
Maximum sum of subarray is =  208
Total avergae runtime:  0.022179698944091795


=============== ARRAY OF SIZE 100 ===============
Maximum sum of subarray is =  300
Maximum sum of subarray is =  527
Maximum sum of subarray is =  943
Maximum sum of subarray is =  942
Maximum sum of subarray is =  622
Maximum sum of subarray is =  721
Maximum sum of subarray is =  754
Maximum sum of subarray is =  731
Maximum sum of subarray is =  661
Maximum sum of subarray is =  684
Total avergae runtime:  0.06560792922973632


=============== ARRAY OF SIZE 500 ===============
Maximum sum of subarray is =  1555
Maximum sum of subarray is =  1945
Maximum sum of subarray is =  1590
Maximum sum of subarray is =  1783
Maximum sum of subarray is =  712
Maximum sum of subarray is =  1471
Maximum sum of subarray is =  792
Maximum sum of subarray is =  694
Maximum sum of subarray is =  1060
Maximum sum of subarray is =  1778
Total avergae runtime:  4.920056986808777


=============== ARRAY OF SIZE 1000 ===============
Maximum sum of subarray is =  3371
Maximum sum of subarray is =  1913
Maximum sum of subarray is =  2578
Maximum sum of subarray is =  2616
Maximum sum of subarray is =  1601
Maximum sum of subarray is =  965
Maximum sum of subarray is =  2934
Maximum sum of subarray is =  1278
Maximum sum of subarray is =  1807
Maximum sum of subarray is =  3308
Total avergae runtime:  41.01500475406647
'''
