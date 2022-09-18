m=int(input())
n=int(input())
for i in range(m,n+1):
    t=i
    sum=0
    while i!=0:
        r=i%10
        sum = sum*10+r
        i //=10
    if sum==t:
        print(t,end=' ')
        