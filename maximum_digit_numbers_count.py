def digits(n):
    dig=0
    if n<0:
        n = -n 
    while n!=0:
        n //=10
        dig += 1
    return dig
n=int(input())
lst=list(map(int,input().split()))
l=[]
dig=0
for i in lst:
    if digits(i)>=dig:
        dig=digits(i)
for j in lst:
    if digits(j)==dig:
        print(j,end=' ')