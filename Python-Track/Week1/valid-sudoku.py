class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        
     
        for i in board:
            count_row = Counter(i)

            for key,val in count_row.items():
                if key != "." and val > 1:
                    return False
        
        column = list(zip(*board))

        for j in column:
            count_col = Counter(j)

            for key, val in count_col.items():
                if key != "." and val > 1:
                    return False

        sub_box = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != "." and  board[row][col] in sub_box[(row//3,col//3)]:
                    return False
                
                sub_box[(row//3 , col//3)].add(board[row][col])


        return True