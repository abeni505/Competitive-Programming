class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
 
        run_sum = 0
        for i in range(len(nums)):
            run_sum += nums[i]
            nums[i] = run_sum

        return nums


