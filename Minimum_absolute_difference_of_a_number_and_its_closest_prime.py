def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count +=1
    return count
n=int(input())
m=p=n
if prime(n)==2:
    print(0)
else:
    while prime(n)!=2:
        n+=1
    x=(n-m)
    while prime(m)!=2:
        m -= 1
    y=(p-m)
    if x<y:
        print(x)
    else:
        print(y)