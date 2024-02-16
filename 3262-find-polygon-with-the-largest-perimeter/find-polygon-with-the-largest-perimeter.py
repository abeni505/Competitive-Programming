class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
       
        run_sum = 0
        max_len = -1
        for i in range(len(nums)):
            if i >= 2 and run_sum > nums[i]:
                max_len = max(max_len , run_sum + nums[i])

            run_sum += nums[i]

        return max_len
