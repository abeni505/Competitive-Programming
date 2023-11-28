class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)-1):
            for column in range(len(matrix[row])-1):
                
                if matrix[row][column] != matrix[row+1][column+1]:
                    return False
        return True
                    