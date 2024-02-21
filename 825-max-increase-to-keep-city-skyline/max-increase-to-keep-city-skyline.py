class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        transposed = list(zip(*grid))

        row = len(grid)
        col = len(grid[0])

        total = 0
        for r in range(row):
            for c in range(col):
                new = min(max(grid[r]) , max(transposed[c]))
                total += abs(grid[r][c] - new)
                grid[r][c] = new


        return total