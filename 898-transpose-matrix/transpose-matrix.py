class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        row = len(matrix)
        col = len(matrix[0])
        out_put = []
       
        for i in range(col):
            new_row = []
            for j in range(row):
                new_row.append( matrix[j][i] )

            out_put.append(new_row)
            
        return out_put