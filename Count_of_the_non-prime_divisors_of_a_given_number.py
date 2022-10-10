def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+= 1
    return count
n=int(input())
l=[]
for j in range(1,n+1):
    if n%j==0 and prime(j)!=2:
        l.append(j)
print(len(l))