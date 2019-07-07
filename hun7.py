n1=int(input())
n2=list(map(int,input().split()))
x=[]
for i in range(0,len(n2)):
 if n2[i]%2==0 and i%2==1:
  x.append(n2[i])
 elif n2[i]%2==1 and i%2==0:
  x.append(n2[i])
print(*x,sep=' ')
