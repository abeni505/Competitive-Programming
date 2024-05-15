class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        def inbound(row,col):
            return 0 <= row < n and 0 <= col < n

        memo = {}
        def dp(row, col):
            if (row,col) in memo:
                return memo[(row,col)]

            if not inbound(row,col):
                return float('inf')
            if row == n - 1:
                return matrix[row][col]
            
            d_left =  dp(row + 1 , col - 1)
            d_right = dp(row + 1 , col + 1)
            down =  dp(row + 1 , col)


            memo[(row,col)] = matrix[row][col] + min(d_left , d_right , down)
            return memo[(row,col)]
        
        minn = float('inf')
        for i in range(n):
            minn = min(minn, dp(0 , i))
        
        return minn