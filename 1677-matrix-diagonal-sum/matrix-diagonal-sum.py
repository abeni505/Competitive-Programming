class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        total_sum = 0

        for i in range(len(mat)):

            total_sum += mat[i][i]
            if i != len(mat)-i-1: # to skip the diagonal
                total_sum += mat[i][len(mat)-i-1]

        return total_sum