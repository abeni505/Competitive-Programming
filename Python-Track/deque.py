# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

N=int(input())

d=deque()
for i in range(N):
    command,*value=input().split()
    if command=="append":
        d.append(*value)
    if command=="pop":
        d.pop()
    if command=="popleft":
        d.popleft()
    if command=="appendleft":
        d.appendleft(*value)
        
print(*d)
