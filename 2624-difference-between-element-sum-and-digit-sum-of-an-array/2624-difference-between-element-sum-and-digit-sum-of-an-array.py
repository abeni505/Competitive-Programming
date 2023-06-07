class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        z=""
        for i in nums:
            elementsum=sum(nums)
            z+="".join(str(i))
            
        digitsum=0
        for i in z:
            digitsum+=int(i)
        return abs(elementsum-digitsum)
       