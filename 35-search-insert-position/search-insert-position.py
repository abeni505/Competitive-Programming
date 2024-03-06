class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        indx = bisect.bisect_right(nums,target)

        if nums[indx - 1] == target:
            return indx - 1
        return indx