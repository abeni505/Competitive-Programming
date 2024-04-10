class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        row = len(mat)
        col = len(mat[0])

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col

        distance = [[float('inf') for c in range(col)] for r in range(row)]

        drxn = [(-1,0),(1,0),(0,1),(0,-1)]

        queue = deque()
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    distance[r][c] = 0


        while queue:
            x , y = queue.popleft()

            for a , b in drxn:
                newx = x + a
                newy = y + b

                if inbound(newx,newy) and distance[newx][newy] == float('inf'):
                    distance[newx][newy] = distance[x][y] + 1
                    queue.append((newx,newy))

        return distance

