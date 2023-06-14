class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left=0
        right=0
        while right<len(nums):
            if nums[right] % 2==0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1
           
            

        return nums