class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        total = 0
        
        for i in range(len(mat)):

            left_sum = mat[i][i]

            right_sum = mat[i][len(mat) - 1 - i]
            if i == len(mat) - 1 - i:
                right_sum = 0

            total += left_sum + right_sum

        return total