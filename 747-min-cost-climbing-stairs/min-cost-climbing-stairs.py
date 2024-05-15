class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]

            if i >= n:
                return 0
            
            first = cost[i] + dp(i + 1)
            second = cost[i] + dp(i + 2)
            
            memo[i] = min(first , second)
            return memo[i]
        
        return min(dp(0),dp(1))