class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])

        row_1 = [0] * m
        col_1 = [0] * n

        for i in range(m):
            for j in range(n):
                row_1[i] += grid[i][j]
                col_1[j] += grid[i][j]

        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (row_1[i] + col_1[j]) - m - n

        return grid

