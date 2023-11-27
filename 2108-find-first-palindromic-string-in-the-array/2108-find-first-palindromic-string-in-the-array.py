class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        ans = ""
        
        for s in words:
            if s == s[::-1] and ans == "":
                return ans.join(s)
                
        return ans
        