n=int(input())
lst=list(map(int,input().split()))
sum=0
while n!=0:
    for i in lst:
        sum += i*2**(n-1)
        n -= 1
print(sum)