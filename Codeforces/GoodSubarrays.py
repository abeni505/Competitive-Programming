from collections import defaultdict
t = int(input())
 
for _ in range(t):
    n = int(input())
    s = list(map(int,input()))
 
    
    prefix = defaultdict(int)
    prefix[0] = 1
    
    count = pre_right = 0
    for i in range(len(s)):
 
        pre_right += s[i]
        pre_left = pre_right - i - 1
        count += prefix[pre_left]
 
        prefix[pre_left] += 1
   
    print(count)