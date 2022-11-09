n=input()
v=c=d=s=0
for i in n:
    if i in 'aeiouAEIOU':
        v += 1
    elif i==' ':
        s += 1
    elif i in '0123456789':
        d += 1
    else:
        c += 1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',s)