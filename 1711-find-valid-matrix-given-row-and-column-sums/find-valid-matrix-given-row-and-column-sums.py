class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        mat = [[0]* len(colSum) for _ in range(len(rowSum))] 

        print(mat)
        row = len(mat)
        col = len(mat[0])


        for r in range(row):
            for c in range(col):
                mat[r][c] = min(rowSum[r] ,colSum[c]) 
                rowSum[r] -= mat[r][c]
                colSum[c] -= mat[r][c]

        return mat