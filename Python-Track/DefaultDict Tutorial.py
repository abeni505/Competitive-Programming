# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m=list(map(int,input().split()))

groupA=defaultdict(list)


for i in range(n):
    keyA=input()    
    groupA[keyA].append(i+1)
    
for i in range(m):
    keyB=input() 
    if keyB in groupA:
        print(*groupA[keyB])
    else:
        print(-1)   
  
    

