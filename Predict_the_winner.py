n=int(input())
l=list(map(int,input().split()))
x=y=0
for i in range(n):
    if(i%2==0):
        x =x+l[i]
    else:
        y=y+l[i]
d=abs(x-y)
if(d%4==0):
    print("X")
else:
    print("Y")