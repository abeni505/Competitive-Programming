class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ans = []
        n = len(heights)
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(ans, diff)
            if len(ans) > ladders:
                bricks = bricks-heapq.heappop(ans)
            if bricks < 0:
                return i
        
        return n-1