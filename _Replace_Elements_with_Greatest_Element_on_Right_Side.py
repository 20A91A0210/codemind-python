n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    maxi=0
    for j in range(i+1,n):
        maxi=max(maxi,l[j])
    l[i]=maxi
l[n-1]=-1
print(*l)    
        