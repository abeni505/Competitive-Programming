class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s_arr = list(S)
        left = 0
        right = len(s_arr) - 1
        while left < right:
            if not s_arr[left].isalpha():
                left += 1
                continue
            
            if not s_arr[right].isalpha():
                right -= 1
                continue
            
            s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
            left += 1
            right -= 1
        return "".join(s_arr)
