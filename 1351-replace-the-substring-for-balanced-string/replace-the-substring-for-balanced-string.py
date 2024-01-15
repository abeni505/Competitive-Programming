class Solution:
    def balancedString(self, s: str) -> int:
        
        count = Counter(s)
        req_amount = len(s)//4
        left = 0
        min_len = float('inf')

        for right in range(len(s)):
            count[s[right]] -= 1

            while all(val <= req_amount for val in count.values()) and left < len(s):
                min_len = min(min_len , right - left + 1)
                count[s[left]] += 1
                left += 1


        if min_len == float('inf'):
            return 0
        return min_len
