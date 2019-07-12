from collections import OrderedDict
jk=str(input())
def remove_duplicate(jk):
    return "".join(OrderedDict.fromkeys(jk))
print(remove_duplicate(jk))
