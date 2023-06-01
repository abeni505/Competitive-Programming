class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_index=i
            for j in range(i+1,len(nums)):
                if nums[min_index]>nums[j]:
                    min_index=j

            nums[i],nums[min_index]=nums[min_index],nums[i]

        return nums
            