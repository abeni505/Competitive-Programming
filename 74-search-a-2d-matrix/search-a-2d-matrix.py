class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        together = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                together.append(matrix[r][c])

        indx = bisect_left(together,target)

        return together[indx] == target if indx < len(together) else False