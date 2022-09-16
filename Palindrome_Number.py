t=int(input())
for i in range(t):
    n=int(input())
    x=n
    sum = 0
    while n!=0:
        r=n%10
        sum = sum*10+r
        n //=10
    if sum==x:
        print('True')
    else:
        print('False')
        