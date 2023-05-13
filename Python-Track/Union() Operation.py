# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
eng=set(input().split())
b=input()
fren=set(input().split())

union=eng.union(fren)
print(len(union))

