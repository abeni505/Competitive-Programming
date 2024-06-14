class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        maxheap = []
        heapify(maxheap)
        nums.sort()

        hashset = set()
        count = 0
        
        for i in range(len(nums)):
            if nums[i] in hashset:
                toadd = -heappop(maxheap)
                tobe = toadd + 1 - nums[i]
                nums[i] += tobe
                count += tobe

                heappush(maxheap, -toadd)
            hashset.add(nums[i])
            heappush(maxheap , - nums[i])

        return count