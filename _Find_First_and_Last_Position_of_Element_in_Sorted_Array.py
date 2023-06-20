n=int(input())
l=list(map(int,input().split()))
k=int(input())
lst=[]
c=0
if k not in l:
    lst.append(-1)
    lst.append(-1)
    c=1
if(c==1):
    print(*lst)
for i in range(n):
    if l[i]==k:
        lst.append(i)
        break
for j in range(n):
    if (l[j]==k and l[j+1]!=k) or (l[j]==k and j==n-1):
        lst.append(j)
        break
if(len(l)==0):
    lst.append(-1)
    lst.append(-1)
if(c==0):
    print(*lst)