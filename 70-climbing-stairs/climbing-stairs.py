memo = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 4:
            return n
        
        if n in memo:
            return memo[n]
        
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        memo[n] = ans

        return memo[n] 