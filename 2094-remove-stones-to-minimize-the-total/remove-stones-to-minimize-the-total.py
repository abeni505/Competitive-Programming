class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        maxheap = [-i for i in piles]
        heapify(maxheap)

        for _ in range(k):
            
            heappush(maxheap , heappop(maxheap)//2)
        
        return sum(maxheap) * -1