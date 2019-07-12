m1=int(input())
m2=list(map(int,input().split()))
print(m2.index(min(m2))+1,end=" ")
print(m2.index(max(m2))+1)

