mn=int(input())
rever=""
while mn>0:
  lastdigit=mn%10
  rever=rever+str(lastdigit)
  mn=mn//10
print(rever)
