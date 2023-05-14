# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
arr=list(map(int,input().split()))
setA=set(map(int,input().split()))
setB=set(map(int,input().split()))



count=0
for i in arr:
    if i in setA:
        count+=1
    elif i in setB:
        count-=1
        
print(count )
