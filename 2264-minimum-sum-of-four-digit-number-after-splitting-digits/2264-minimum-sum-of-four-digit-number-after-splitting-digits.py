class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
       
        numstr=sorted(str(num))
        
        num1=int(numstr[0]+numstr[2])
        num2=int(numstr[1]+numstr[3])

        return num1+num2