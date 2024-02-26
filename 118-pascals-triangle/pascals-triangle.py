class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        triangle = self.generate(numRows - 1)
        prevRow = triangle[-1]

        newRow = [1]
        for i in range(1,len(prevRow)):
            newRow.append(prevRow[i] + prevRow[i - 1])

        newRow.append(1)
    
        res = triangle + [newRow]
    
        return res



            