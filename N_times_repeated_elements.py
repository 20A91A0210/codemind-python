n=int(input())
lst=list(map(int,input().split()))
k=int(input())
l=[]
for i in lst:
    x=lst.count(i)
    if x==k:
        l.append(i)
if len(l)==0:
    l.append(-1)
l=list(set(l))
print(*l)