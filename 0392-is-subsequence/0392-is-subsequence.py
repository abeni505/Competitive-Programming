class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0
        second = 0
        
        while first < len(s) and second < len(t):
            
            if s[first] == t[second]:
                first += 1
                
            second += 1
            
            
        if first == len(s):
            return True
        
        return False
        