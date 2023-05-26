class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_new=sorted(s)
        t_new=sorted(t)

        if s_new == t_new:
            return True
        else:
            return False




     
    
