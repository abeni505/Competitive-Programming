class Solution:
    def totalMoney(self, n: int) -> int:
        
        week = n // 7
        remain = n % 7

        total = 28*(week) + 7*(week-1)*week//2
        total += remain*(week + 1) + remain*(remain - 1)//2
        
        return total