class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        right=1
     
        for left in range(0,len(nums),2):
            if nums[left]%2!=0:
                while nums[right]%2!=0:
                    right+=2
                nums[left],nums[right]=nums[right],nums[left]
                
            
        return nums



                