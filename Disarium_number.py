def dn(x):
    y=x
    l=[]
    while x!=0:
        r =x%10
        l.append(r)
        x //=10
    l=len(l)
    sum=0
    while y!=0:
        t= y%10
        sum =sum + t**l
        l -=1
        y //=10
    return sum
n=int(input())
if dn(n)==n:
    print('True')
else:
    print('False')