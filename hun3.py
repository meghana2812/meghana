m=int(input())
z=list(map(int,input().split()))
a=[]
for i in range(0,m):
    if z[i]==i:
        a.append(i)
        a.sort()
if len(a)>0:
    for u in a:
        print(u,end=" ")
else:
    print(-1)
