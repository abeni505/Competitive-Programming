class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])

        row_1 = [0] * m
        col_1 = [0] * n
        row_0 = [0] * m
        col_0 = [0] * n
        
        out_put = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_1[i] += 1
                    col_1[j] += 1
                else:
                    row_0[i] += 1
                    col_0[j] += 1

        for i in range(m):
            for j in range(n):
                out_put[i][j] = row_1[i] + col_1[j] - row_0[i] - col_0[j]

        return out_put

