class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = {}
        def dp(indx):
            if indx in memo:
                return memo[indx]

            if indx >= len(questions):
                return 0

            take = questions[indx][0] + dp(indx + questions[indx][1] + 1)
            not_take = dp(indx + 1)

            memo[indx] = max(take,not_take)
            return memo[indx]
        
        
        return dp(0)