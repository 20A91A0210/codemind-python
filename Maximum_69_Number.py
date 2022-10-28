n=int(input())
l=[]
while n!=0:
    r =n%10
    l.append(r)
    n//=10
l.reverse()
for i in range(len(l)):
    if l[i]==6:
        l[i]=l[i]+3
        break
num=0
for i in l:
    num = num*10+i
print(num)