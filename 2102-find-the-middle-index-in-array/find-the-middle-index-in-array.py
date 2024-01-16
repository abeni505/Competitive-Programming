class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = [nums[0]]

        for i in range(1,len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])


        for j in range(len(nums)):
            prefix = pre_sum[j] - nums[j]
            suffix = pre_sum[-1] - pre_sum[j]

            if prefix == suffix:
                return j
        
        return -1