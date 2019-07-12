h=int(input())
count=0
for i in range (0,h+1):
    s=str(i)
    for j in range (0,len(s)):
        if (s[j]=='2'):
            count+=1
print(count)        
