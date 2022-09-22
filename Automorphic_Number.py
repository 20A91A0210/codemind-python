n=int(input())
r=n
x=n**2
y=x
num=0
while n!=0:
    n //= 10
    num +=1
z=x//10**num
y=x-(z*10**num)
if y==r:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
        
    