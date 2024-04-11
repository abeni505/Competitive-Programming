class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        row , col = len(grid) , len(grid)
        start, end = (0,0), (row - 1,col - 1)

        drxn = [(-1, 0),(1, 0),(0, 1),(0, -1),(1, 1),(-1, -1),(1, -1),(-1, 1)]

        def inbound(r , c):
            return 0 <= r < row and 0 <= c < col


        if grid[0][0] != 0:
            return -1



        queue = deque([(0, 0)])
        grid[0][0] = 1

        distance = 1
        while queue:

            for _ in range(len(queue)):
                a , b = queue.popleft()

                    
                if (a , b) == end:
                    return distance
                for x , y in drxn:
                    newr = a + x
                    newc = b + y

                    if inbound(newr, newc) and grid[newr][newc] == 0:
                        
                        queue.append((newr , newc))
                        grid[newr][newc] = 1
        
            distance += 1
        return -1
