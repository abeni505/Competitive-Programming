class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)
        col = len(matrix[0])

        prefix = [[0]*(col + 1) for _ in range(row + 1)]

        for r in range(row):
            for c in range(col):
                left = prefix[r][c - 1]
                top = prefix[r - 1][c]
                diagonal_left = prefix[r - 1][c - 1]

                prefix[r][c] = left + top - diagonal_left + matrix[r][c]

        # print(prefix)
        
        ans = 0
        for r_top in range(row):
            for r_bottom in range(r_top , row):
                count = defaultdict(int)
                count[0] = 1
                for c in range(col):
        
                    top = prefix[r_top - 1][c]
                    # we compute for each column so no need for left  and diagonal_left

                    curr_sum = prefix[r_bottom][c] - top 
                    diff = curr_sum - target
                    ans += count[diff]

                    count[curr_sum] += 1
                    

        return ans