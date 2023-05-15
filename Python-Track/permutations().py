# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s,k=input().split()


perm=sorted(permutations(s,int(k)))

for i in perm:
    print("".join(i))
