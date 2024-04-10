class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        row , col = len(grid), len(grid[0])

        def inbound(r , c):
            return 0 <= r < row and 0 <= c < col

        drxn = [(-1,0),(1,0),(0,1),(0,-1)]
        
        fresh = time = 0
        queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

      
        while queue and fresh:

            time += 1
            for _ in range(len(queue)):
                x , y = queue.popleft()

                for a , b in drxn:
                    newx = a + x
                    newy = b + y

                    if inbound(newx,newy) and grid[newx][newy] == 1:
                        fresh -= 1
                        grid[newx][newy] = 2
                        queue.append((newx,newy))

        if not fresh:
            return time

        return -1

                
