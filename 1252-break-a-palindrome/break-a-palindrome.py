class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
       
        p = list(palindrome)

        if len(p) == 1:
            return ""

        left = 0
        right = len(p)//2
        while left < right:
            if p[left] != "a":
                p[left] = "a"
                break
            else:
                left += 1
        else:
            p[-1] = "b"

        return("".join(p))
      
