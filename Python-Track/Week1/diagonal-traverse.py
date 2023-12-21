class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        diagonals = defaultdict(list)

        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])

        output = []

        for key, val in diagonals.items():
            if  key % 2 != 0:
                output.extend(diagonals[key])
                
            else:   
                output.extend(diagonals[key][::-1])
                
        return output