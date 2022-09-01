n=int(input())
k=n
sum=0
while n!=0:
    x=n%10
    sum =sum*10+x
    n //= 10
if sum==k:
    print('True')
else:
    print('False')