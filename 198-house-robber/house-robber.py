class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        dp[len(nums)-1] = nums[len(nums)-1]
        dp[len(nums)-2] = nums[len(nums)-2]

        for right in range(len(nums) - 3 , -1 , -1):
            dp[right] = max(nums[right], nums[right] + max(dp[right + 2:]))

        return max(dp)