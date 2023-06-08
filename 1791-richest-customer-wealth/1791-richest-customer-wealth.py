class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max=0
        for i in accounts:
            summ=sum(i)
            if summ>=max:
                max=summ

        return max