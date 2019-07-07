x1,x2=map(int,input().split())
a=[]
for j in range(x1+1,x2+1):
  if j>1:
    for k in range(2,j):
      if(j%k==0):
        break
    else:
      a.append(k)
print(len(a)+1)
