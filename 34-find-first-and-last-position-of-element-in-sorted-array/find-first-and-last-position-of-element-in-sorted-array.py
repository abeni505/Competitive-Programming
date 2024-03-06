class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        right = bisect.bisect_right(nums,target)
        left = bisect.bisect_left(nums,target)

        # print(left , right)
        if left < len(nums) and right > 0 and nums[left] == target:
            return [left,right -1]
        return [-1,-1]

