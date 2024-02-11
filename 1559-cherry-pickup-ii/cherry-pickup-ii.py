class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        memo = {}

        def dfs(self,r,c1,c2):
            if (r,c1,c2) in memo:
                return memo[(r,c1,c2)]

            if c1 == c2 or min(c1,c2) < 0 or max(c1,c2) >= col:
                return 0
            if r == row - 1:
                return grid[r][c1] + grid[r][c2]

            drxn = [-1,0,1]
            ans = 0
            for robot_1 in drxn:
                for robot_2 in drxn:
                    ans = max(ans, dfs(self, r + 1 ,c1 + robot_1 ,c2 + robot_2))

            # ans += grid[r][c1] + grid[r][c2]
            memo[(r,c1,c2)] = ans + grid[r][c1] + grid[r][c2]
            return memo[(r,c1,c2)]
            
        return dfs(self, 0, 0, col - 1)