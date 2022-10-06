n=int(input())
m=n
s=str(n)
l=list(s)
y=len(l)
sum=0
while n!=0:
    r=n%10
    z=y
    sum =sum+r**z
    n //=10
    y -= 1
if sum==m:
    print('True')
else:
    print('False')