na,nb=input().split()
X=abs(len(na)-len(nb))
for v in range(len(na)):
    if len(nb)==1 and nb[v] in na:
        break
    if na[v]!=nb[v]:
        X+=1
print(X)
