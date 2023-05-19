#Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
s=input().split()
    
print(all(int(i)>0  for i in s)  and  any(  j[::-1]==j    for j in s   ))
