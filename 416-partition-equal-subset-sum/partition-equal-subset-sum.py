class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)

        if s % 2: 
            return False 

        target = s // 2

        memo = {}
        def dp(i, target):
            if (i, target) in memo:
                return memo[(i, target)]

            if target == 0: 
                return True

            if i >= n or target < 0:
                return False
            
            memo[(i, target)] = dp(i + 1, target - nums[i]) or dp(i + 1, target)

            return memo[(i,target)]

        return dp(0, target)