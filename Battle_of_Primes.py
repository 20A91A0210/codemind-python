def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count += 1
    return count
n1=int(input())
n2=int(input())
x=1
y=n1+n2+x
while prime(y)!=2:
   x += 1
   y=n1+n2+x
print(x)
    