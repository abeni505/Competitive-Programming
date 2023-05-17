# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N=int(input())

data=namedtuple('data',input())
ls=[]
s=0

for i in range(N):
    x=input().split()
    ls.append(data(*x))
  
    
for i in range(N):
    s+=int(ls[i].MARKS)
print(s/N)
