class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
       
        for r in range(1,n):
            for c in range(n):
                top_left = matrix[r-1][c-1] if c - 1 >= 0 else float('inf')
                top_up = matrix[r-1][c]
                top_right = matrix[r-1][c+1] if c + 1 <= n - 1 else float('inf')

                matrix[r][c] = matrix[r][c] + min(top_left,top_up,top_right)

        return min(matrix[-1])