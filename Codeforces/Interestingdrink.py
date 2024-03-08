import bisect
n = int(input())

nums = list(map(int,input().split()))

k = int(input())
nums.sort()

for _ in range(k):
    
    target = int(input())

    indx = bisect.bisect_right(nums,target)

    print(indx)