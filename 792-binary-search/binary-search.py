class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        indx = bisect.bisect_right(nums,target)

        if indx > 0 and nums[indx - 1] == target:
            return indx -1 
        else:
            return -1