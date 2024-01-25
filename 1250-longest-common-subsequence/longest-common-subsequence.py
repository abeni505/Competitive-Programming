class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        row = len(text1)
        col = len(text2)
        
        dp = [[0 for c in range(col + 1)] for r in range(row + 1)]

        for r in range(row):
            for c in range(col):
                if text1[r] == text2[c]:
                    dp[r][c] = dp[r - 1][c - 1] + 1
                else:
                    
                    dp[r][c] = max(dp[r - 1][c] , dp[r][c - 1])


        return dp[r][c]