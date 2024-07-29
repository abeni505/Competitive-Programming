class Solution:
    def numTeams(self, rating: List[int]) -> int:
        K = 3

        @cache
        def dp(i, depth = 1, reverse = True):
            if depth == K: return 1
            res = 0
            for j in range(i + 1, len(rating)):
                if (reverse and rating[j] > rating[i]) or (not reverse and rating[j] < rating[i]):
                    res += dp(j, depth + 1, reverse)
            return res

        res = 0
        for i in range(len(rating)):
            res += dp(i, reverse = True) 
            res += dp(i, reverse = False) 

        return res