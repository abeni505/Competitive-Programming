class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        x = defaultdict(list)

        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                x[i+j].append(mat[i][j])

        output = [*x[0]]
        for key, val in x.items():
            if key > 0 and key % 2 != 0:
                for i in x[key]:
                    output.append(i)
            elif key > 0 and key % 2 == 0:
                reverse = x[key]
                for i in reverse[::-1]:
                    output.append(i)

        return output