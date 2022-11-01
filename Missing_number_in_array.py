t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    for i in range(1,n+1):
        if i not in lst:
            print(i)