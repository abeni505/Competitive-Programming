class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=1
        n=len(nums)

        while right<n:
            if nums[left]==nums[right]:
                right+=1
            else:
                nums[left+1]=nums[right]
                left+=1
        return left+1
    


    
            