g,h=input().split()
if(len(g)==len(h)):
      for i in g:
          u=g.count(i)
      for i in h:
          v=h.count(i)
      if(u==v):
        print("yes")
      else:
        print("no")
else:
   print("no")
