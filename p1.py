w= int(input())
a=[]
for i in range(0,word):
 in=input()
 b.append(in)
li=[]
for i in zip(*a):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
 
 else:
  break
print(''.join(li))
