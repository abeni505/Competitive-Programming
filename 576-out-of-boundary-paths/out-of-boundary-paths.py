class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        memo = {}
        def rec(r , c , maxMove):
            if (r , c , maxMove) in memo:
                return memo[(r , c , maxMove)]

            if r < 0 or c < 0 or r >= m or c >= n:
                return 1

            if maxMove == 0:
                return 0

            drxn = [(-1,0),(0,-1),(1,0),(0,1)]

            ans = 0
            for x , y in drxn:
                ans += rec(r + x, c + y , maxMove - 1)
            memo[(r , c , maxMove)] = ans

            return ans

        return rec(startRow , startColumn , maxMove) % (10**9 + 7)


