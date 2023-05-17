# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N=int(input())
od=OrderedDict()

for i in range(N):
    string =input().split()
    key=" ".join(string[:-1])
    value=int(string[-1])
    
    if key in od:
        od[key]=od[key]+value
    else:
        od[key]=value
    
    
for key,value in od.items():
    print(key,value)
