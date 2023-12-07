class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        range_sum = sum(range(0,len(nums) + 1))
        
        return range_sum - total_sum