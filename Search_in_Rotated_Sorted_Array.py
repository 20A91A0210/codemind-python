n=int(input())
l=list(map(int,input().split()))
t=int(input())
c=0
for i in range(n):
    if(l[i]==t):
        print(i)
        c=1
        break
if(c==0):
    print(-1)
