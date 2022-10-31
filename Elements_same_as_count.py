n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if i==lst.count(i):
         l.append(i)
l1=[]
if len(l)!=0:
       for i in l:
           if i not in l1:
               l1.append(i)
       print(*l1)
else:
    print(-1)