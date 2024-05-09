class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        maxheap = [-i for i in happiness]
        heapify(maxheap)

        original = k

        ans = 0
        while maxheap and k:
            ans += max(0 ,(heappop(maxheap) * -1) - (original - k))
            k -= 1


        return ans
                    

