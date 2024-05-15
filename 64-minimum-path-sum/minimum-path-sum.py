class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        def inbound(row , col):
            return 0 <= row < n and 0 <= col < m

        memo = {}
        def dp(row , col):
            if (row,col) in memo:
                return memo[(row,col)]

            if not inbound(row , col):
                return float('inf')

            if row == n - 1 and col == m - 1:
                return grid[row][col]       
        
            memo[(row, col)] = grid[row][col] + min(dp(row + 1 , col) ,dp(row,col + 1))
            return memo[(row, col)]

        return dp(0,0)
                    

