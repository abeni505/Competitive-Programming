class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum=[*nums]
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+ nums[i]

        for i in range(len(nums)):
            left_sum=prefix_sum[i]-nums[i]
            right_sum=prefix_sum[-1]-prefix_sum[i]

            if left_sum==right_sum:
                return i
        return -1
            
