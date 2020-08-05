def exhaustive_nuts_bolts(a,b):
    for i in range(len(a)):
        for j in range(len(a)):
            if(b[j]==a[i]):
                b[i],b[j]=b[j],b[i]
                break


a=[5,4,1,7,3]
b=[1,3,4,5,7]
exhaustive_nuts_bolts(a,b)
print("Matched nuts and bolts:")
print(a,b)

'''
Matched nuts and bolts:
[5, 4, 1, 7, 3] [5, 4, 1, 7, 3]
'''
