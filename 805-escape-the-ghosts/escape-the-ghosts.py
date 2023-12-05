class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        my = abs(target[0])  + abs(target[1])

        for i in range(len(ghosts)):
            x1, y1 = ghosts[i]
            x2, y2 = target[0],target[1]
            print(x2,y2)
            if abs(x2 - x1) + abs(y2 - y1) <= my:
                return False

        return True