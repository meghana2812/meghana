mn=int(input())
ar=list(map(int,input().split()))
c=len(ar)
big=max(ar)
x,y=0,0
for i in range(0,c-1):
    for j in range(i+1,c):
        if abs(ar[i]+ar[j])< big:
            g,h=ar[i],ar[j]
            big=abs(x+y)
print(x,y)
