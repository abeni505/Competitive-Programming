class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        nums=[]
        new=""
        for i in s:
            nums.append(i[-1])
        nums.sort()
        for i in nums:
            for j in s:
                if i==j[-1]:

                    new += j[0:-1] + ' '
        new = new.rstrip()
        return new
