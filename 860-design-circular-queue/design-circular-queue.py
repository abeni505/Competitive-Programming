class MyCircularQueue:

    def __init__(self, k: int):
        self.circularqueue = []
        self.k = k
    

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False 
        if len(self.circularqueue) < self.k:
            self.circularqueue.append(value)
            return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if len(self.circularqueue) > 0:
            self.circularqueue.pop(0)
            return True
        

    def Front(self) -> int:
        if len(self.circularqueue) > 0:
            return self.circularqueue[0]
        return -1
        

    def Rear(self) -> int:
        if len(self.circularqueue) > 0:
            return self.circularqueue[-1]
        return -1
        

    def isEmpty(self) -> bool:
        
        return len(self.circularqueue) == 0
        

    def isFull(self) -> bool:
        return len(self.circularqueue) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()