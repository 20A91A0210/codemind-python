def prime(n):
    prime=True
    if n==1:
        prime=False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
    return prime
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if prime(i)==True:
        c +=1 
print(c)