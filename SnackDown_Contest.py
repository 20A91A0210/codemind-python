t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    l=[]
    for i in p:
        if i not in l:
            l.append(i)
    for i in q:
        if i not in l:
            l.append(i)
    if len(l)==n:
        print('YES')
    else:
        print('NO')
    