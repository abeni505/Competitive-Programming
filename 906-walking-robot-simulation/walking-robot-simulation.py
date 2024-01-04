class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        directions = [(0,1) , (-1,0) ,(0,-1) , (1,0)] # N W S E

        obs = set()

        for a , b in obstacles:
            obs.add((a,b))

        max_ = 0
        current = 0
        x , y = 0 , 0
        for c in commands:
            if c == -2:
                current = (current + 1) % 4
            elif c == -1:
                current = (current + 3) % 4
            else:
                for _ in range(c):
                    curx , cury = directions[current]
                    newx , newy = x + curx , y + cury

                    if (newx , newy) in obs:
                        break
                    
                    x = newx
                    y = newy
                
                max_ = max(max_, x*x + y*y)

        return max_
