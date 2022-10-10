def reverse(x):
    rev=0
    while x!=0:
        r = x%10
        rev=rev*10+r
        x //=10
    return rev
n=int(input())
x=m=n
n +=1
while reverse(n)!=n:
    n +=1
y=n-m
x -=1

while reverse(x)!=x:
    x -= 1
z=m-x
if y==z:
    print(x,n)
elif y>z:
    print(x)
else:
    print(n)