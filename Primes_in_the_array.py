def prime(n):
    prime=True
    if n==1:
        prime=False
    if n==2:
        prime =True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
    return prime
n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if prime(i)==True:
        c+= 1
print(c)

