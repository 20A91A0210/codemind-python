def hn(x):
    sum=0
    while x!=0:
        r = x%10
        sum = sum+ r**2
        x //=10
    return sum
n=int(input())
while n>9:
    n=hn(n)
if n==1 or n==7:
    print(True)
else:
    print(False)