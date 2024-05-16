class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        days = set(days)
        last_day = max(days)

        memo = {}
        def dp(day):
            if day in memo:
                return memo[day]

            if day > last_day:
                return 0

            if day in days:
                memo[day] = min(costs[0] + dp(day + 1), costs[1] + dp(day + 7), costs[2] + dp(day + 30))
     
            else:
                memo[day] = dp(day + 1)      
           
            return memo[day]
        
        return dp(0)
