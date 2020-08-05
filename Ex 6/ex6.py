def trace_lcs(tab,a,b):
    i=len(a)
    j=len(b)
    lcs=[]
    while(i>0):
        if(tab[i][j]==tab[i-1][j]):
                i=i-1
        elif(tab[i][j-1]==tab[i][j]):
                j=j-1
        else:
            lcs.append(a[i-1])
            i=i-1
            j=j-1
    print("Longest subsequence:",lcs)

def longest_subsequence(a,b):
    tab=[]
    lcs=[]
    for i in range(len(a)+1):
        tab.append([0]*(len(b)+1))
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if(a[i-1]==b[j-1]):
                tab[i][j]=tab[i-1][j-1]+1
            else:
                tab[i][j]=max(tab[i-1][j],tab[i][j-1])
    print("Length of the longest subsequence:",tab[len(a)][len(b)])
    trace_lcs(tab,a,b)


a=[1,8,2,9,3,4,0]
b=[1,67,89,2,90,3,4]
longest_subsequence(a,b)

"""
a=[3,9,80,67]
b=[1,2,4,5]
Length of the longest subsequence: 0
Longest subsequence: []


a=[1,8,2,9,3,4,0]
b=[1,67,89,2,90,3,4]
Length of the longest subsequence: 4
Longest subsequence: [4, 3, 2, 1]
"""
