class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        row = len(matrix)
        col = len(matrix[0])

        return [[matrix[j][i] for j in range(row)] for i in range(col)]