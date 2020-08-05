def mat_power(x,n): 
    if n==0:
        return 1
    if (n%2)!=0:
        result = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(len(A)): 
   for j in range(len(A[0])): 
      for k in range(len(A)): 
         result[i][j] += A[i][k] * A[k][j]
         x=result
        return x*fast_power(x,n-1)
    else:
        return fast_power(x,n/2)*fast_power(x,n/2)



A=[]
n=int(input("Enter N for N x N matrix: "))         
print("Enter the element ::>")
for i in range(n): 
   row=[]                                      
   for j in range(n): 
      row.append(int(input()))         
      A.append(row)                     
print(A)
print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(A[i][j], end=" ")
   print()                                                                               

mat_power(A,n)

