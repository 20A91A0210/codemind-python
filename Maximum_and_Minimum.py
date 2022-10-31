n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if i==lst.count(i):
         l.append(i)
if len(l)!=0:
       l=list(set(l))
       print(min(l),max(l))
else:
    print(-1)