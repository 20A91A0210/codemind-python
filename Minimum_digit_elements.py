def dig(n):
    dig=0
    while n!=0:
        dig += 1
        n //= 10
    return dig
n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    x=dig(i)
    l.append(x)
y=min(l)
print(l.count(y))