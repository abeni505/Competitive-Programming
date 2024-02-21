class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        max_len = 0
        count = Counter(s)

        odd = False

        for val in count.values():
            if val & 1:
                odd = True
                max_len += val -1
            else:
                max_len += val
        if odd:
            max_len += 1
            
        return max_len
