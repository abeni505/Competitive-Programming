class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
       
        n = len(matrix)
    
        for c in range(n):
            for r in range(n // 2): # to not swap again 
                matrix[r][c], matrix[n - 1 - r][c] = matrix[n - 1 - r][c], matrix[r][c]

        for row in range(n):
            for col in range(row + 1): # to swap from above main digonal
                matrix[row][col] , matrix[col][row] = matrix[col][row] , matrix[row][col]

        # for row in matrix:
        #     print(row)
        
