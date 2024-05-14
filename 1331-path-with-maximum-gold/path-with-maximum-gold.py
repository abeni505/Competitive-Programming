class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        drxn = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def backtrack(row, col):
            if not inbound(row, col) or grid[row][col] == 0:
                return 0
            max_gold = 0
            original_val = grid[row][col]
            grid[row][col] = 0

            for dr, dc in drxn:
                next_row = row + dr
                next_col = col + dc
                max_gold = max(max_gold, backtrack(next_row, next_col))

            grid[row][col] = original_val
            return max_gold + original_val

        for row in range(rows):
            for col in range(cols):
                max_gold = max(max_gold, backtrack(row, col))
                
        return max_gold
