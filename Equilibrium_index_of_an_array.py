t=int(input())
for i in range(t):
    ans=0
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(1,n):
        l[i]=l[i]+l[i-1]
    for j in range(n):
        if(l[j-1]==l[n-1]-l[j]):
            ans=j
    if(ans==0):
        ans=-1
    print(ans)