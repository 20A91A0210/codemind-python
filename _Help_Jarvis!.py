t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    m=0
    while(n!=0):
        r=n%10
        m += 1
        l.append(r)
        n = n//10
    l.sort()
    c=0
    for i in range(m-1):
        if (l[i]+1!=l[i+1]):
            c += 1
            break
    if(c==0):
        print("YES")
    else:
        print("NO")
    # print(l)
        