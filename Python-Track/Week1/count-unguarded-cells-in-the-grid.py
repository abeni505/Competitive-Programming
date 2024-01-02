class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        mat = []
        for row in range(m):
            row = []
            for col in range(n):
                row.append(1)
            mat.append(row)

        for row, col in guards:
            mat[row][col] = "G"
        for row, col in walls:
            mat[row][col] = "W"

        
        for row in range(m):

            curr = 1
            for col in range(n):
                if mat[row][col] == "G":
                    curr = "x"
                elif mat[row][col] == "W":
                    curr = 1
                elif mat[row][col] == 1:
                    if curr == "x":
                        mat[row][col] = "x"

        for row in range(m):

            curr = 1
            for col in range(n - 1, -1 , -1):
                if mat[row][col] == "G":
                    curr = "x"
                elif mat[row][col] == "W":
                    curr = 1
                elif mat[row][col] == 1:
                    if curr == "x":
                        mat[row][col] = "x"

        for col in range(n):

            curr = 1
            for row in range(m):
                if mat[row][col] == "G":
                    curr = "x"
                elif mat[row][col] == "W":
                    curr = 1
                elif mat[row][col] == 1:
                    if curr == "x":
                        mat[row][col] = "x"

        for col in range(n):

            curr = 1
            for row in range(m - 1, -1 , -1):
                if mat[row][col] == "G":
                    curr = "x"
                elif mat[row][col] == "W":
                    curr = 1
                elif mat[row][col] == 1:
                    if curr == "x":
                        mat[row][col] = "x"

        count = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    count += 1

        # print(mat)
        return count
