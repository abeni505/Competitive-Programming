class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = [nums[0]]

        for i in range(1,len(nums)):
            run_sum.append(nums[i] + run_sum[-1])

        return run_sum

    