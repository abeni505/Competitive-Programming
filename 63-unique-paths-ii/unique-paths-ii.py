class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1]:
            return 0

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        memo = {}
        def dp(row, col):

            if (row , col) in memo:
                return memo[(row,col)]

            if row == m-1 and col == n-1:
                return 1
            
            if not inbound(row , col) or obstacleGrid[row][col] == 1:
                return 0

            memo[(row,col)] = dp(row + 1, col) + dp(row , col + 1)
            return memo[(row,col)]

        return dp(0,0)