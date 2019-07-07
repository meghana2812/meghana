d = input()
dl = list(d)
for i in range(0,len(dl),2) :
    dl[i],dl[i+1]=dl[i+1],dl[i]
swap = ''.join(dl)
print(swap)
