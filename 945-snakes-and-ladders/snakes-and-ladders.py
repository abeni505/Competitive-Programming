class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        board.reverse()
        n = len(board)

        def function(value):
            row = (value - 1) // n
            col = (value - 1) % n
            if row % 2 != 0:
                col = n - 1 - col
            return (row, col)

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        next_ = [1, 2, 3, 4, 5, 6]
        visited = set()
        queue = deque([(1, 0)])
        visited.add(1)
       
        while queue:
            curr, count = queue.popleft()
            
            if curr == n * n:
                return count

            for nbr in next_:
                newc = curr + nbr

                if newc > n * n:
                    continue

                r, c = function(newc)
                
                if inbound(r, c):
                    final_value = board[r][c] if board[r][c] != -1 else newc
                    if final_value not in visited:
                        queue.append((final_value, count + 1))
                        visited.add(final_value)
                        
        return -1


    

