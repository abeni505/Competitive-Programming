from collections import deque
from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        def inbound(r , c):
            return 0 <= r < len(land) and 0 <= c < len(land[0])

        drxn = [(-1,0),(1,0),(0,1),(0,-1)]

        queue = deque([])
        visited = set()
        output = []
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col] == 1 and (row, col) not in visited:
                    queue.append((row, col))
                    visited.add((row, col))

                    max_row = row
                    max_col = col

                    while queue:
                        curr_row, curr_col = queue.popleft()

                        for a, b in drxn:
                            newr = curr_row + a
                            newc = curr_col + b

                            if inbound(newr, newc) and land[newr][newc] == 1 :
                                if (newr, newc) not in visited:
                                    queue.append((newr, newc))
                                    visited.add((newr, newc))

                                    max_row = max(max_row, newr)
                                    max_col = max(max_col, newc)

                    output.append([row, col, max_row, max_col])

        return output
