class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        max_array = []
        hashset = set()
       
        nums.sort()

        count = 0
        for i in range(len(nums)):
            if nums[i] in hashset:
                
                tobe = max_array[-1] + 1 - nums[i]
                nums[i] += tobe
                count += tobe

                
            hashset.add(nums[i])
            max_array.append(nums[i])

        return count