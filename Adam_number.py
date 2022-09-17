n=int(input())
x=n**2
temp =n
rev=0
while n!=0:
    r=n%10
    rev =rev*10  +r
    n //= 10
y=rev**2
rev_of_y=0
while y!=0:
    x=y%10
    rev_of_y = rev_of_y*10+x
    y //=10
if rev_of_y==temp**2:
    print('True')
else:
    print('False')
    