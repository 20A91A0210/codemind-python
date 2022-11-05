n=int(input())
lst=list(map(int,input().split()))
sf=ss=0
for i in range(n//2):
    x=lst[i]
    sf += x
for j in range(n//2,n):
    y=lst[j]
    ss += y
print(abs(sf-ss))