def cm(x):
    
  if not x: return ''
  s1 = min(x)
  s2 = max(x)
  for i, c in enumerate(s1):
    if c != s2[i]:
      return s1[:i]
  return s1
def main():
  a=int(input())
  ad=[]
  for i in range(0,a):
    e=input()
    ad.append(e)
  y1=cm(asd) 
  print(y1)
  
if __name__== "__main__":
  main()
