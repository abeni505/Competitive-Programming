class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        drxn = [(0, 1),(0, -1), (-1, 0),(1, 0)]

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"

        count = 0

        def dfs(row, col):
            for a , b in drxn:
                newr = row + a
                newc = col + b
            
                if inbound(newr, newc):
                   
                    grid[newr][newc] = "0"
                    dfs(newr , newc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == "1" :
                    grid[row][col] = "0"
                    dfs(row , col)
                    count += 1
        return count

                            


                    