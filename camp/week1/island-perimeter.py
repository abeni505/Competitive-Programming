class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        drxn = [(0 , 1),(0 , -1),(1 , 0),(-1 , 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print(row,col)
                if grid[row][col] == 1:
                    count += 4

                    for a , b in drxn:
                        newr = row + a
                        newc = col + b

                        if inbound(newr,newc) and grid[newr][newc] == 1:
                            count -= 1
        
        return count
                            

                        
