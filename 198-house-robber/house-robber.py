class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for left in range(2, len(nums)):
            dp[left] = max(nums[left], nums[left] + max(dp[:left - 1]))

        return max(dp)