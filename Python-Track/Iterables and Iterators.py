# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
from itertools import combinations
N=int(input())
s=input().split()
k=int(input())


counter=0
s=list(itertools.combinations(s,k))
for i in range(len(s)):
    if "a" in list(s[i]):
        counter+=1
        
        
print(counter/len(s))
