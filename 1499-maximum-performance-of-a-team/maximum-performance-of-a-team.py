class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
     
        arr = sorted(zip(efficiency, speed), reverse=True)
        ans, tot, heap, mod = 0, 0, [], pow(10, 9) + 7
        for i in range(n):
            heappush(heap, arr[i][1])
            tot += arr[i][1]
            if len(heap) > k:
                tot -= heappop(heap)
            ans = max(ans, tot * arr[i][0])
            
        return ans % mod
        