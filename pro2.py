from itertools import combinations
m,y = input().split()
y = int(y)
num = []
d = combinations(n,len(m)-y)
for i in d:
    num.append("".join(i))
print(min(num))
