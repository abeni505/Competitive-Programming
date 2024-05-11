class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        workers = sorted((wage[i] / quality[i], quality[i]) for i in range(len(quality)))

        minheap = []
        minn = float('inf')

        curr_q = 0
        for ratio , quality in workers:
            heappush(minheap, -quality)

            curr_q += quality
            if len(minheap) > k:
                curr_q += heappop(minheap)
            
            if len(minheap) == k:
                minn = min(minn, curr_q * ratio)

        return minn

