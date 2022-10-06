def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count += 1
    return count
n=int(input())
d=[]
npd=[]
for j in range(1,n+1):
    if n%j==0:
        d.append(j)
for k in d:
    if prime(k)!=2:
        npd.append(k)
print(len(npd))