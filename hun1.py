x=int(input())
y=list(map(int,input().split()))[:x]
a=[]
for i in range(len(y)):
    k=i+1
    for j in range(k,len(y)) :
        
        if(y[i]==y[j] and y[i] not in a):
            a.append(y[i])
a.sort()
if(a):
    for i in a:
        print(i,end=" ")
else:
    print("unique")
