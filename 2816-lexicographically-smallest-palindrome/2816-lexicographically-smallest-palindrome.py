class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        right=len(s)-1

        while left<=right:
            if s[left]!=s[right]:
                if s[left]<s[right]:
                    s=s[:right]+s[left]+s[right+1:]
                else:
                    s=s[:left]+s[right]+s[left+1:]
            left+=1
            right-=1
        
        return s
