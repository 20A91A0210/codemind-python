n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    t=a[i]+b[i]
    c.append(t)
print(*c)