# Enter your code here. Read input from STDIN. Print output to STDOUT
sizeA=int(input())
setA_elements=map(int,input().split())
sizeB= int(input())
setB_elements=map(int,input().split())

setA=set(setA_elements)
setB=set(setB_elements)

symdiff = list(setA.symmetric_difference(setB))
symdiff.sort()

for i in symdiff:
    print(i)
