n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if i%2==0:
        l.append(i)
m=1
for j in lst:
    if j%2!=0:
        l.insert(m,j)
        m += 2
if len(l)%2!=0:
    l.append(0)
print(*l)
        
        