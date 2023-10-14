class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        range_arr=[i for i in range(len(nums)+1)]
        for i in range_arr:
            if i not in nums:
                return i
        