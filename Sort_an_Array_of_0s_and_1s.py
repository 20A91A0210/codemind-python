n=int(input())
lst=list(map(int,input().split()))
l=[]
l1=[]
for i in lst:
    if(i==0):
        l.append(i)
    else:
        l1.append(i)
for i in l1:
    l.append(i)
print(*l)