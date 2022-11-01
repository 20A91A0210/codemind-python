n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    j=i*i
    l.append(j)
l.sort()
print(*l)