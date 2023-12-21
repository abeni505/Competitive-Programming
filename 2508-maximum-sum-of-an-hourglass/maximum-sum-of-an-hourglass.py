class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

    
        row = len(grid)
        col = len(grid[0])

        max_sum = 0
        for r in range(1,row-1):
            for c in range(1,col-1):
                I_sum = (grid[r-1][c-1] + grid[r-1][c] + grid[r-1][c+1] + grid[r][c] +
                         grid[r+1][c-1] + grid[r+1][c] + grid[r+1][c+1])

                max_sum = max(max_sum,I_sum)
        return max_sum


        