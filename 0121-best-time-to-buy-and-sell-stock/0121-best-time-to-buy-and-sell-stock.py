class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy=0
        sell=1
        profit=0

        while sell<=len(prices)-1:
            if prices[buy]>prices[sell]:
                buy=sell
            else:
                profit=max(profit,prices[sell]-prices[buy])
            sell+=1
            
        return profit
       