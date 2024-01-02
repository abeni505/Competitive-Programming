class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_arr = []
        for i in s:
            if i.isalnum():
                new_arr.append(i.lower())
        new_s = "".join(new_arr)
        
        left = 0
        right = len(new_s) - 1

        while left < right:
            if new_s[left] != new_s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True