n = int(input())

nums = list(map(int,input().split()))
speed = list(map(int,input().split()))

dist_speed = [[nums[i],speed[i]] for i in range(n)]

dist_speed.sort(key = lambda x :x[0])
# print(dist_speed)

def calc(target):
    interval = []
    max_ = float("-inf")
    min_ = float("inf")
    for x , v in dist_speed:
        op = target * v 
        left = x - op 
        right =  x + op

        max_ = max(max_,left)
        min_ = min(min_ ,right)
        interval.append((left , right))

    if min_ >= max_:
        return True
    return False

left = 0
right = 10e9 + 1

while left + (10**(-6)) < right:
    mid = (left + right)/2

    if calc(mid):
        right = mid
    else:
        left = mid

print(right)

