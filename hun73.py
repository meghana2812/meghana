sp1=input()
sp2=input()
sp3=""
for i in range(len(sp1)):
    for j in range(len(sp1),-1,-1):
        if sp1[i:j] in sp2:
            if len(sp1[i:j])>=len(sp3):
                sp3=sp1[i:j]
print(sp3)
