n=int(input())
lst=list(map(int,input().split()))
s_e=s_o=0
for i in lst:
    if i%2==0:
        s_e+=i
    elif i%2!=0:
        s_o +=i
print(abs(s_e-s_o))
        