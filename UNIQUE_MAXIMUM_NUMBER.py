n=int(input())
lst=list(map(int,input().split()))
num=0
l=[]
for i in lst:
    if lst.count(i)==1:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(max(l))
        