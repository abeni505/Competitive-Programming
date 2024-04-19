class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            heappush(self.maxheap, -num)
            temp = heappop(self.maxheap)
            heappush(self.minheap, -temp)
        else:
            heappush(self.minheap, num)
            temp = heappop(self.minheap)
            heappush(self.maxheap, -temp)
        
    def findMedian(self) -> float:
 
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0])/2
        else:
            return self.minheap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian() 