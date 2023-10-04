def roman(n):
    if(n=="I"):
        return 1
    elif n=="V":
        return 5
    elif n=="X":
        return 10
    elif n=="L":
        return 50
    elif n=="C":
        return 100
    elif n=="D":
        return 500
    elif n=="M":
        return 1000
s=input()
ans=0;
for i in range(len(s)-1,-1,-1):
    if(i!=len(s)-1 and roman(s[i])<roman(s[i+1])):
        ans -= roman(s[i])
    else:
        ans += roman(s[i])
print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    