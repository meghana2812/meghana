w=int(input())
s=0
m=len(str(w))
while w>0:
    a=int(n)%10
    s=s+(a**m)
    w=w//10
print(s)
