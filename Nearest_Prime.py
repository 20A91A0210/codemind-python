def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+= 1
    return count
t=int(input())
for i in range(t):
    n=int(input())
    x=m=n
    while prime(n)!=2:
        n += 1
    y=n-m
    while prime(x)!=2:
        x -= 1
    z=m-x
    if y>z:
        print(x)
    elif y<z:
        print(n)
    elif y==z:
        if x>n:
            print(n)
        else:
            print(x)