a=list(map(int,input().split()))
b=list(map(int,input().split()))
a1=b1=0
for i in range(3):
    if a[i]>b[i]:
        a1 += 1
    elif a[i]<b[i]:
        b1+=1
print(a1,b1)
    