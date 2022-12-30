n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
t=int(input())
total=n
for i in l:
    if i>t:
        total += 1
print(total)