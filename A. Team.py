n=int(input())
totalcount=0
count=0
for i in range(n): 
    pts=list(map(int,input().split()))
    for i in pts:
        if i==1:
            count+=1
            
    if count>=2:
        totalcount+=1
    count=0
            
print(totalcount)

    
        
