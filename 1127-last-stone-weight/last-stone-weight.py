class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
      
        heap = [-i for i in stones]
        heapify(heap)
  
        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)

            if x != y:
                heappush(heap , x - y)

        if not heap:
            return 0
        
        return -1 * (heap[0] )