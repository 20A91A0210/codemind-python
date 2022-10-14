n=int(input())
a=0
b=1
l=[]
while len(l)<n:
    l.append(a)
    if len(l)<n:
          l.append(b)
    a = a+b
    b = a+b
print(*l)