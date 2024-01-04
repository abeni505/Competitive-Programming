class Robot:

    def __init__(self, width: int, height: int):
        self.directions = [(1,0),(0,-1),(-1,0),(0,1)] # E S W N
        self.labels = ["East","South","West","North"]
        self.width = width
        self.height = height
        self.x , self.y = 0 , 0
        self.current = 0

    def step(self, num: int) -> None:
        # to remove cycle 
        total = ((self.height+self.width-2)*2)
        num = num % total

        if num == 0:
            num += (self.height+self.width-2)*2
        
        for _ in range(num):
            dx , dy = self.directions[self.current]
            nx , ny = self.x + dx , self.y + dy

            while not (0 <= nx < self.width  and 0 <= ny < self.height):
                self.current = (self.current + 3) % 4
                dx , dy = self.directions[self.current]
                nx , ny = self.x + dx , self.y + dy
               
            self.x = nx
            self.y = ny

    def getPos(self) -> List[int]:     
        return [self.x , self.y]
        

    def getDir(self) -> str:
        return self.labels[self.current]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()