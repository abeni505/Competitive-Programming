class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod=1
        summ=0
        for i in str(n):
            prod*=int(i)
            summ+=int(i)

        return prod-summ