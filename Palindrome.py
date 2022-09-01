n=int(input())
sum=0
k=n
while n!=0:
    x=n%10
    sum = sum*10+x
    n //= 10
if sum==k:
    print('True')
else:
    print('False')