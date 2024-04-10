class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        drxn = [(-1,0),(1,0),(0,1),(0,-1)]
        def inbound(r , c):
            return 0 <= r < row and 0 <= c < col

        max_area = 0
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    stack = [(r,c)]
                    visited.add((r,c))

                    curr_area = 0
                    while stack:
                        curr_area += 1
                        x , y = stack.pop()

                        for a , b in drxn:
                            newx = x + a
                            newy = y + b

                            if inbound(newx,newy) and grid[newx][newy] == 1:
                                if (newx,newy) not in visited:
                                    stack.append((newx, newy))
                                    visited.add((newx, newy))
                                    
                    max_area = max(max_area , curr_area)
                    
        return max_area


