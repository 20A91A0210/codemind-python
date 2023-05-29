def prime(n):
    if(n<2):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
prime_product=1
nonprime_product=1
for i in l:
    if(prime(i)==True):
        prime_product *= i
    else:
        nonprime_product *= i
print(abs(prime_product-nonprime_product))