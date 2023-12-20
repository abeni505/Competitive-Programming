class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()
        sum_ = prices[0] + prices[1]
        if sum_ > money:
            return money
        return money - sum_