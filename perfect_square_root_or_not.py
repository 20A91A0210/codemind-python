n=int(input())
s=0
for i in range(1,n):
    if n==i**2:
        s+=1
if s==1:
    print('True')
else:
    print('False')