class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dp(ind, curr):
            if ind == len(triangle):
                return 0
            if (ind, curr) not in memo:
                memo[(ind, curr)] = min(dp(ind + 1, curr) + triangle[ind][curr],dp(ind + 1, curr + 1) + triangle[ind][curr])
            return memo[(ind, curr)]

        return dp(0, 0)
