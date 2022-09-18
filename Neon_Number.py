n=int(input())
x=n**2
sum=0
while x!=0:
    r= x%10
    sum += r
    x//=10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')
    