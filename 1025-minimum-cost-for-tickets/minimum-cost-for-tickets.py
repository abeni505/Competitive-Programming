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
    
            minn = float('inf')

            if day in days:
                for i in range(3):
                    if i == 0:
                        minn = min(minn, costs[i] + dp(day + 1))
                    elif i == 1:
                        minn = min(minn , costs[i] + dp(day + 7))
                    else:
                        minn = min(minn, costs[i] + dp(day + 30))
                    
                    memo[day] = minn
            else:
                memo[day] = dp(day + 1)
                
           
            return memo[day]
        
        return dp(0)
