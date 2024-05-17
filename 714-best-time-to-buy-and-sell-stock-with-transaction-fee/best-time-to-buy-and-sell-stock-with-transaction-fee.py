class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        memo = {}
        def dp(indx , buying):
            if (indx, buying) in memo:
                return memo[(indx, buying)]

            if indx >= n:
                return 0
            
            if buying:
                buy = dp(indx + 1 , not buying) - prices[indx] 
                leave = dp(indx + 1, buying)

                memo[(indx, buying)] = max(buy , leave)

            else:
                sell = (prices[indx] + dp(indx + 1, not buying)) - fee
                leave = dp(indx + 1, buying)

                memo[(indx, buying)] = max(sell, leave)

            return memo[(indx, buying)]

        return dp(0, True)