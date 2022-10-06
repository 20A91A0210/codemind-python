def sdn(x):
    y=x
    l=[]
    lst=[]
    while x!=0:
        r=x%10
        l.append(r)
        x//=10
    for i in l:
        if i==0:
            break
        elif y%i==0:
            lst.append(i)
    if len(l)==len(lst):
        p=1
    else:
        p=2
    return p
        
m=int(input())
n=int(input())
for j in range(m,n+1):
    if sdn(j)==1:
        print(j,end=' ')