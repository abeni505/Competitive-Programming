class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        left = max_len = count = 0

        for right in range(len(s)):
            count += abs(ord(s[right]) - ord(t[right])) 

            while count > maxCost:
                count -= abs(ord(s[left]) - ord(t[left])) 
                left += 1
               
            max_len = max(max_len , right - left + 1)

        return max_len