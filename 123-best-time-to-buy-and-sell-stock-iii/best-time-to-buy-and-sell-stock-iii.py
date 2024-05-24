class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        memo = {}
        def dp(indx , buying, count):
            if (indx, buying , count) in memo:
                return memo[(indx, buying, count)]

            if indx >= n or count == 2:
                return 0
            
            if buying:
                buy = dp(indx + 1 , not buying, count) - prices[indx] 
                leave = dp(indx + 1, buying, count)

                memo[(indx, buying, count)] = max(buy , leave)

            else:
                sell = prices[indx] + dp(indx + 1, not buying, count + 1)
                leave = dp(indx + 1, buying, count)

                memo[(indx, buying,count)] = max(sell, leave)

            return memo[(indx, buying,count)]

        return dp(0, True, 0)