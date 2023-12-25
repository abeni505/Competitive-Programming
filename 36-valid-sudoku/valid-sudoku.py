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

        for row in range(9):
            for col in range(9):
                
                count = 0
                row_index = row // 3
                col_index = col // 3
                
                for r in range(row_index * 3 , (row_index * 3) + 3):
                    for c in range(col_index * 3 ,(col_index * 3) + 3):
                        if board[r][c] != "." and board[r][c] == board[row][col]:
                            if count >= 1:
                                return False
                            count += 1

        return True