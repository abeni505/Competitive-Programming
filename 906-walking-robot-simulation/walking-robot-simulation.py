class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        obs = set()
        max_distance = 0

        for x , y in obstacles:
            obs.add((x,y))

        current = 0
        x , y = 0 , 0
        for c in commands:
            if c == -2:
                current = (current - 1) % 4
            elif c == -1:
                current = (current + 1) % 4
            else:
                for _ in range(c):
                    dx , dy = directions[current]
                    xn  , yn = x + dx , y + dy

                    if (xn , yn) in obs:
                        break

                    x , y = xn , yn
                max_distance = max(max_distance , x*x + y*y)

        return max_distance