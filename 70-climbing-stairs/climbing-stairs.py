class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n
        
        dp = [2 , 3]
        
        i = 4
        while i <= n:
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp

            i += 1
        
        return dp[1]