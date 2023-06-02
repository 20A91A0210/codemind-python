t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    lx=list(map(int,input().split()))
    ly=list(map(int,input().split()))
    for j in ly:
        lx.append(j)
    lx.sort()
    print(*lx)