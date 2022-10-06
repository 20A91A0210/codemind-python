def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count += 1
    return count
n=int(input())
l=[]
for j in range(1,n+1):
    if n%j==0 and prime(j)==2:
        l.append(j)
        if len(l)==2:
            break
        else:
            continue
if len(l)<2:
    print(-1)
else:
    p=1
    for k in l:
        p *= k
    if p==n:
        for k in l:
            print(k,end=' ')
    else:
        print(-1)

        
    
        