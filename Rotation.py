t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    temp=0
    for j in range(k):
        temp=l[n-1]
        l.remove(l[n-1])
        l.insert(0,temp)
    print(*l)
        
        