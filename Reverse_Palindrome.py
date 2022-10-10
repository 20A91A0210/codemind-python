def reverse(x):
    rev=0
    while x!=0:
        r=x%10
        rev=rev*10+r
        x//=10
    return rev
x=int(input())
x += reverse(x)
while x!=reverse(x):
     x += reverse(x)
print(x)