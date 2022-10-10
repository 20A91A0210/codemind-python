def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+= 1
    return count
def reverse(x):
    rev=0
    while x!=0:
        r = x%10
        rev= rev*10+r
        x //= 10
    return rev
n=int(input())
if prime(n)==2:
    if prime(reverse(n))==2:
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')