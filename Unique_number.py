n=int(input())
l=[]
while n!=0:
    r=n%10
    l.append(r)
    n //=10
s=set(l)
l1=list(s)
if len(l)==len(l1):
    print('Unique Number')
else:
    print('Not Unique Number')