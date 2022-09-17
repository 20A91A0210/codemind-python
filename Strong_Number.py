n=int(input())
s=str(n)
l=list(s)
s=[]
sum =0
for i in l:
    x=int(i)
    p =1
    for j in range(x,0,-1):
        p *= j
    s.append(p)
for j in s:
    sum +=j
if sum==n:
    print('The number',n,'is a strong number')
else:
    print('The number',n,'is not a strong number')