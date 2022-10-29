n=int(input())
lst=list(map(int,input().split()))
s_o=s_e=0
for i in range(len(lst)):
    if i%2==0:
        s_e += lst[i]
    elif i%2 !=0:
        s_o += lst[i]
print(abs(s_e-s_o))
        