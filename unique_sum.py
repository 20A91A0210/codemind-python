n=int(input())
lst=list(map(int,input().split()))
lst=list(set(lst))
print(sum(lst))