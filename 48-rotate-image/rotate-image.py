class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        n = len(matrix)

        for r in range(n):
            for c in range(r + 1):
                matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]

        for row in matrix:
            row.reverse()

        
        
        
