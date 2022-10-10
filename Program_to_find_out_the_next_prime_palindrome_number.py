def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+= 1
    return count
def reverse(x):
    rev=0
    while x !=0:
        r =x%10
        rev = rev*10+r
        x //= 10
    return rev
n=int(input())
n+=1
while reverse(n)!=n or prime(n)!=2 :
        n+=1
print(n)