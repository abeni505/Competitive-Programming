class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        heap = []

        for i in range(1,len(heights)):
            
            diff = heights[i] - heights[i - 1]

            if diff > 0:
                heappush(heap , diff)
            
            if len(heap) > ladders:
                used = heappop(heap)

                if used > bricks:
                    return i - 1
                else:
                    bricks -= used

        return len(heights) - 1

        
    