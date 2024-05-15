class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        minn = prices[0]
        maxx = 0

        for i in range(1 , n):
            maxx = max(maxx , prices[i] - minn)
            minn = min(minn, prices[i])

        return maxx

