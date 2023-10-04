s=input()
maxi=0
for i in s:
    if s.count(i)>maxi:
        maxi=s.count(i)
m=0
ans=""
for i in s:
    if (s.count(i)>m and s.count(i)!=maxi):
        m=s.count(i)
        ans = i
if(m==0):
    print(-1)
else:
    print(ans)