# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))

N= int(input())

for i in range(N):
    cmd,*value=input().split()
    
    if cmd =="pop":
        s.pop()
    elif cmd=="remove":
        s.remove(int(value[0]))
    elif cmd=="discard":
        s.discard(int(value[0]))
  


print(sum(s))
