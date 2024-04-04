class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        drxn = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()
        stack = [(0, 0)]

        while stack:
            row, col = stack.pop()
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                return True  

            visited.add((row, col))
            for a, b in drxn[grid[row][col]]:
                newr = row + a
                newc = col + b
                if inbound(newr, newc) and (newr, newc) not in visited:
                    check = grid[newr][newc]
                    for x, y in drxn[check]:
                        if (newr + x, newc + y) == (row, col):
                            stack.append((newr, newc))
                            
        return False