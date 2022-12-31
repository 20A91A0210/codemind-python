s=input()
s=s.lower()
count=0
for i in s:
    if i==' ' and s.count(i)==1:
        count-=1
    if s.count(i)==1:
        count+= 1
print(count)
    