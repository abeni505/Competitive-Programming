class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
       
        p = list(palindrome)
        left = 0
        right = len(p)-1
        while left < right:
            if p[left] == p[right] and p[left] != "a":
                p[left] = "a"
                left += 1
                right -= 1
                break
            else:
                left += 1
                right -= 1

        else:
            if left >= right:
                p[-1] = "b"
        if len(p) == 1:
            return ""
        else:
            return("".join(p))
      
