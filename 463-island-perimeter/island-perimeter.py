class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        drxn = [(0, 1),(0, -1),(1, 0),(-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    stack = [(row,col)]

                    while stack:
                        r , c = stack.pop()
                        for a , b in drxn:
                            newr = r + a
                            newc = c + b

                            if not inbound(newr,newc) or grid[newr][newc] == 0:
                                count += 1
        
        return count
                            

                        
