class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.rsplit(maxsplit = 2)
        
        return len(s[-1])