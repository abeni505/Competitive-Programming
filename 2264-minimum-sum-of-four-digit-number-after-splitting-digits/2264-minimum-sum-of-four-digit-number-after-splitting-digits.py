class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
       
        numstr=sorted(str(num))
        nums="".join(numstr)
        
        num1=int(nums[0]+nums[2])
        num2=int(nums[1]+nums[3])

        return num1+num2