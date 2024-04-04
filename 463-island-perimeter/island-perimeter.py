class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        drxn = [(0, 1),(0, -1),(1, 0),(-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        
        count = 0
        def dfs(row, col):
            nonlocal count
            for a, b in drxn:
                newr = row + a
                newc = col + b

                if inbound(newr, newc) and  grid[newr][newc] == 1 :

                    if (newr, newc) not in visited:
                        visited.add((newr, newc))
                        dfs(newr, newc)
                
                else:
                    count += 1
              
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:

                    visited.add((row, col))
                    dfs(row, col)

        return count


                        
