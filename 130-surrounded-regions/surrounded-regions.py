class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        def inbound(row , col):
            return 0 <= row < n and 0 <= col < m

        drxn = [(-1,0),(1,0),(0,1),(0,-1)]

        visited = set()
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and (r in [0, n - 1] or c in [0, m - 1]):
                    stack = [(r,c)]
                    visited.add((r,c))
                    board[r][c] = "#"
                    while stack:
                        row , col = stack.pop()

                        for a , b in drxn:
                            newr = row + a
                            newc = col + b

                            if inbound(newr,newc) and board[newr][newc] == "O":
                                if (newr,newc) not in visited:
                                    stack.append((newr,newc))
                                    visited.add((newr,newc))
                                    board[newr][newc] = "#"

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O' 
