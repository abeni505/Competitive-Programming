class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        curr_sum = 0
        def dp(i , curr_sum):
            if (i , curr_sum) in memo:
                return memo[(i , curr_sum)]

            if i < 0 and curr_sum == target:
                return 1
            if i < 0:
                return 0

            
            take = dp(i - 1 , curr_sum + nums[i])
            not_take = dp(i - 1, curr_sum - nums[i])

            memo[(i , curr_sum)] =  take + not_take
            return memo[(i, curr_sum)]
        return dp(n - 1, 0)