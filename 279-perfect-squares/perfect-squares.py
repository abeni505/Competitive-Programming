class Solution:
    def numSquares(self, n: int) -> int:
        
        perfect_squares = []

        i = 1
        while i**2 <= n:
            perfect_squares.append(i**2)
            i += 1
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for c in perfect_squares:
                if c <= i:
                    dp[i] = min(dp[i] , 1 + dp[i - c])

        return dp[n]