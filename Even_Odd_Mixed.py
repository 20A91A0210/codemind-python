n=int(input())
s=str(n)
l=list(s)
even=0
odd=0
for i in l:
    if int(i)%2==0:
        even += 1
    else:
        odd += 1
if even>=1 and odd>=1:
    print('Mixed')
elif even>0:
    print('Even')
else:
    print('Odd')