m,n=map(int,input().split())
l=[] 
for i in range(1,m+n):
    if m%i==0 and n%i==0:
        l.append(i)
print(max(l))