class Solution:
    def totalMoney(self, n: int) -> int:

        def weekly(start,end):
            return sum(range(start,end + 1))
        
        full_week = n // 7
        half_week = n % 7

        total_sum = 0
        for i in range(full_week):
            total_sum += weekly(i + 1 , i + 7)

        total_sum += weekly(1 + full_week,half_week + full_week)
    
        return total_sum
