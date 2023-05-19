# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X=map(float,input().split())

marks=[]

for i in range(int(X)):
    marks.append(list(map(float,input().split())))


ziped=zip(*marks)

for i in ziped:
    print(sum(i)/X)
    
