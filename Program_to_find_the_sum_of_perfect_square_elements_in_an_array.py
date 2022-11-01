def ps(n):
    perfsq=False
    for i in range(1,n+1):
            if i*i==n:
                perfsq=True
    return perfsq
n=int(input())
arr=map(int,input().split())
sum=0
for i in arr:
    if ps(i)==True:
        sum += i
print(sum)