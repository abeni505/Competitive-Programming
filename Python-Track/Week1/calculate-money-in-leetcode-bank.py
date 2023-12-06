class Solution:
    def totalMoney(self, n: int) -> int:

        def weekly(start, end):

            return sum(range(start,end+1))

        if n <= 7:
            return weekly(1,n)
        else:
            full_week = n // 7
            remain_day = n % 7

            total = 0
            for day in range(full_week):
                total += weekly(day + 1,day + 7)
            
            total += weekly(1 + full_week ,remain_day + full_week)

        return total

        

        
