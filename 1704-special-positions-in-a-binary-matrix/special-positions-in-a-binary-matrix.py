class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        

        count = 0
        x = len(mat)
        y = len(mat[0])

        for row in range(x):
            for col in range(y):

                if mat[row][col] == 0:
                    continue

                nonzero = True
                for r in range(x):
                    if r != row and mat[r][col] == 1:
                        nonzero = False
                        break
                
                for c in range(y):
                    if c != col and mat[row][c] == 1:
                        nonzero = False
                        break
                        
                if nonzero:
                    count += 1

        return count

