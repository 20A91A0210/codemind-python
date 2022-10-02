n,x=map(int,input().split())
m=n
y=n%(10**x)
count=0
while n!=0:
    count += 1
    n //=10
z=count-x
q=m//(10**z)
if q>y:
    print(q-y)
else:
    print(y-q)