class Solution:
    def minDifference(self, nums):
        if len(nums) < 5:
            return 0

        nums.sort()
        p1 = nums[-1] - nums[3]
        p2 = nums[-2] - nums[2]
        p3 = nums[-3] - nums[1]
        p4 = nums[-4] - nums[0]
        
        return min(p1, p2, p3, p4)