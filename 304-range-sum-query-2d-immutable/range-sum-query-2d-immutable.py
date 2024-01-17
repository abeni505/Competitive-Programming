class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = [[0 for c in range(col +1)]  for r in range(row +1)]

        for r in range(row):
            for c in range(col):
                left_area = self.prefix[r + 1][c]
                right_area = self.prefix[r][c + 1]
                duplicated_area = self.prefix[r][c]
                curr_element = matrix[r][c]

                self.prefix[r + 1][c + 1] =  left_area + right_area - duplicated_area + curr_element
        
       

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 = row2 + 1
        row1 = row1 + 1
        col1 = col1 + 1
        col2 = col2 + 1
        
        Total_area = self.prefix[row2][col2]
        l_area = self.prefix[row2][col1 - 1]
        r_area = self.prefix[row1 - 1][col2]
        dup_area = self.prefix[row1 - 1][col1 - 1]

        return  Total_area - l_area - r_area + dup_area


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)