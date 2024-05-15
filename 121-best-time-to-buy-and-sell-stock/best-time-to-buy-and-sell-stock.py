class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        memo = {}

        def dp(i, min_price):
            if i == n:
                return 0
            
            if (i, min_price) in memo:
                return memo[(i, min_price)]
            
            
            take = prices[i] - min_price
            not_take = dp(i + 1, min(min_price, prices[i]))

            
            memo[(i, min_price)] = max(take, not_take)
            
            return memo[(i, min_price)]

        return dp(0, float('inf'))
