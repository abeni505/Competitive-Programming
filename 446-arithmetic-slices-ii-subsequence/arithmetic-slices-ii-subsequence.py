class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_count, n = 0, len(nums)
        dp  =[defaultdict(int) for _ in range(n)]
        for i in range(1,n):
            for j in range(0,i):
                diff = nums[i]-nums[j]
                
                dp[i][diff] += 1
                if diff in dp[j] :
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]

        return total_count
        