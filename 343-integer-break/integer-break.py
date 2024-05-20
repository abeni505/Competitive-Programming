class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = {}
        def dp(num):
            if num in memo:
                return memo[num]

            if num == 1:
                return 1
            
            ans = 0 if num == n else num
            for i in range(1 , num):
                ans = max(ans, dp(i) * dp(num - i))
            
            memo[num] = ans
            return memo[num]    
    
        return dp(n)