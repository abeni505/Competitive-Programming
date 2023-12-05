class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_len = 0
        for i in range(0,len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                max_len = max(max_len,(nums[i] + nums[i+1] + nums[i+2]))

        return max_len
