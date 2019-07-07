s1,s2=map(str,input().split())
count=0
for x in range(len(s1)):
    if s1[x]!=s2[x]:
        count+=1

if(count==1):
    print("yes")
else:
    print("no")

    
