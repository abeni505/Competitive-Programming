class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        i=1
        while i in nums:
            i+=1
        
        return i
