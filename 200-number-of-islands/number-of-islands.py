class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        drxn = [(0, 1),(0, -1), (-1, 0),(1, 0)]

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1" and (row,col) not in visited:
                    stack = [(row, col)]
                    visited.add((row,col))
                    while stack:
                        r , c = stack.pop()

                        for a , b in drxn:
                            newr = r + a
                            newc = c + b

                            if inbound(newr, newc) and (newr, newc) not in visited and grid[newr][newc] == "1":
                                stack.append((newr,newc))
                                visited.add((newr,newc))

                    count += 1
        return count

                            


                    