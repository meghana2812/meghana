my=input()
ne=''
for i in my:
    if i not in ne:
        ne+=i 
print(ne[::-1])
