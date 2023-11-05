s=input()
ans=""
if s[0] in "aeiouAEIOU":
    ans += "V"
else:
    ans += "C"
for i in range(1,len(s)):
    if s[i] in "aeiouAEIOU":
        if(ans[len(ans)-1]!="V"):
            ans = ans+ "V"
    else:
        if(ans[len(ans)-1]!="C"):
            ans = ans+ "C"
print(ans)