class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        def is_end(i, j): return (i == 0 or j == 0)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] += dp[i + 1][j]
                dp[i + 1][j + 1] += 1 if matrix[i][j] == '1' else 0

        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] += dp[i][j + 1]
        ans =  0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                ni, nj = i, j
                k = 0 
                while not is_end(ni, nj):
                    ones = dp[i][j] - dp[i - (k + 1)][j] - dp[i][j - (k + 1)] + dp[ni - 1][nj - 1]
                    if ones == pow(k + 1, 2):
                        ans = max(ans, pow(k + 1, 2))
                    k += 1
                    ni -= 1
                    nj -= 1
        return ans
        