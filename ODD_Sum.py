n=int(input())
lst=list(map(int,input().split()))
s_e=0
for i in lst:
    if i%2!=0:
        s_e+=i
print(s_e)
        