class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        indx = bisect.bisect_left(nums,target)

        print(indx)
        if indx < len(nums) and nums[indx] == target:
            return indx
        else:
            return -1