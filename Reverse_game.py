def rev(n):
    rev=0
    while n!=0:
        r =n%10
        rev = rev*10+r
        n //= 10
    return rev
n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    x=rev(i)
    lst1.append(x)
print(*lst1)