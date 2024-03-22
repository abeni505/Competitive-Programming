class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])
        
        def inbound(x , y):
            return 0 <= x < row and 0 <= y < col 


        visited = set()

        drxn = [(-1 , 0 ) ,(0 , -1) , (1 , 0) , (0 , 1)]
        def backtrack(x , y , index):
    
            if index == len(word):
                return True

            visited.add((x,y))
            for a , b in drxn:
                r = x + a
                c = y + b
            
                if inbound(r , c) and (r , c ) not in visited and word[index] == board[r][c]:
                    if backtrack(r , c , index + 1):
                        return True

            visited.remove((x,y))
            return False
                    
        for r in range(row ):
            for c in range(col):
                if board[r][c] == word[0] and backtrack(r , c ,1):
                    return True

        return False

