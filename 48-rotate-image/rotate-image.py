class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # row = len(matrix)
        # col = len(matrix[0])

        # rotated = list(zip(*matrix))
        # print(rotated)


        # output = []
        # for i in rotated:
        #     output.append(list(i[::-1]))
        # print(output)
        # return output

        n = len(matrix)
    

        # for r in range(row):
        #     for c in range(col):
        #         temp = matrix[r][c]
        #         matrix[r][c] = matrix[col - 1 - c][ r]
        #         matrix[c][row - 1 - r] = temp
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
        
