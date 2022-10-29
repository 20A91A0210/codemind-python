def rev(n):
    reverse=0
    while n!=0:
        r =n%10
        reverse = reverse*10+r
        n //= 10
    return reverse
n=int(input())
lst=list(map(int,input().split()))
c = 0
for i in lst:
    if rev(i)==i:
        c += 1
print(c)