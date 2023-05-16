# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
no_shoes=int(input())
inventory=list(map(int,input().split()))
no_customer=int(input())

size_available=Counter(inventory)

earn=0
for i in range(no_customer):
    desiredshoe,price=list(map(int,input().split()))
       
    if size_available[desiredshoe]:
       earn += price
       size_available[desiredshoe]-=1
       
       
print(earn)
