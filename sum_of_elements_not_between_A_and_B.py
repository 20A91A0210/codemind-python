n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in lst:
    if a<=i<=b:
        sum=sum
    else:
        sum += i
print(sum)