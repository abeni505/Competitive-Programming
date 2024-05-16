class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n , m = len(text1) , len(text2)
        memo = {}
        def dp(i , j):
            if (i , j) in memo:
                return memo[(i, j)]

            if i == n  or j == m:
                return 0
            
            if i > n or j > m:
                return float('-inf')
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dp(i + 1 , j + 1)
            
            else:
                memo[(i,j)] = max(dp(i + 1, j) , dp(i, j + 1))

            return memo[(i, j)]

        return dp(0,0)