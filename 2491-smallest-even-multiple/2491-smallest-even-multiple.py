class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0:
            smallmul=n
        else:
            smallmul=2*n

            
        return smallmul