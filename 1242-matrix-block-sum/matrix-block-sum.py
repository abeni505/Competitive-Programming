class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])



        for r in range(row):
            for c in range(col):
                left = mat[r][c - 1] if c > 0 else 0
                up = mat[r - 1][c] if r > 0 else 0
                diagonal = mat[r - 1][c - 1] if r > 0 and c > 0 else 0

                mat[r][c] = mat[r][c] + left + up - diagonal
        # print(mat)


        prefix_new = [[0 for c in range(col)] for r in range(row)]

        for i in range(row):
            for j in range(col):
                diagonal_bottom = mat[min(i+k, row-1)][min(j+k, col-1)]
                diagonal_top = mat[i-k-1][j-k-1] if i-k > 0 and j-k > 0 else 0
                top_right = mat[i-k-1][min(j+k, col-1)] if i-k > 0 else 0
                bottom_left = mat[min(i+k, row-1)][j-k-1] if j-k > 0 else 0

                prefix_new[i][j] = diagonal_bottom - top_right - bottom_left + diagonal_top

        # print(prefix_new)

        return prefix_new