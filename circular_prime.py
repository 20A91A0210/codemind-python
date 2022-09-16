n=int(input())
count = 0
for i in range(1,n+1):
    if n%i==0:
        count += 1
if count==2:
    y=5
else:
    y=10
sum =0
x=n
while n!=0:
    r=n%10
    sum =sum*10+r
    n //=10
ncount=0
for j in range(1,sum+1):
    if sum%j==0:
        ncount += 1
if ncount ==2:
    z=5
else:
    z=10
if y==5 and z==5:
    print('circular prime')
elif y==5 or z==5:
    print('prime but not a circular prime')
else:
    print('not prime')