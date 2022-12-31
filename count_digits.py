def digits(n):
    dig=0
    if n<0:
        n = -n
    elif n==0:
        dig=1
    while n!=0:
        n//=10
        dig += 1
    return dig
n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    l.append(digits(i))
print(*l)