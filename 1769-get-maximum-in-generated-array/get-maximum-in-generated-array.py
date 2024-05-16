class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            

            if i % 2:
                return dp(i//2) + dp(i//2 + 1)
            
            else:
                return dp(i//2)
        
        nums = [dp(i) for i in range(1 , n + 1)]

        return max(nums)