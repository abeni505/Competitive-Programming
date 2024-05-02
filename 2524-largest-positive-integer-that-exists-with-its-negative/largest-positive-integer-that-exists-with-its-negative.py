class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        heapify(nums)

        while nums:
            curr = heappop(nums)
            if -curr in nums:
                return abs(curr)
        
        return -1