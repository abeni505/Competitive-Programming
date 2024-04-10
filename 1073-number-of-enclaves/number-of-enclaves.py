class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        drxn = [(-1,0),(1,0),(0,1),(0,-1)]

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col

        count_1 = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    count_1 += 1

        
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited and (r in [0 , row - 1] or c in [0 , col - 1]):
                    stack = [(r,c)]
                    visited.add((r,c))
                    count_1 -= 1

                    while stack:
                        a , b = stack.pop()

                        for x , y in drxn:
                            newx = a + x
                            newy = b + y

                            if inbound(newx,newy) and grid[newx][newy] == 1:
                                if (newx, newy) not in visited:
                                    stack.append((newx,newy))
                                    visited.add((newx,newy))
                                    count_1 -= 1
        
        return count_1

