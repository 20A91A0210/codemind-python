n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in a:
    if i  not in b and i not in l:
        l.append(i)
for j in b:
    if j not in a and j not in l:
        l.append(j)
print(*l)