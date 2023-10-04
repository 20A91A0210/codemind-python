s=input()
l=[]
for i in s:
    if i in "aeiouAEIOU":
        l.append(i)
a=len(l)-1
ans=""
for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
       ans += l[a]
       a -= 1
    else:
        ans += s[i];
print(ans)
        