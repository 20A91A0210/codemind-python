n=int(input())
lst=list(map(int,input().split()))
def sod(n):
    sum=0
    while n!=0:
        r =n%10
        sum += r
        n //= 10
    return sum
sum=0
for i in lst:
    sum +=sod(i)
print(sum)