class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        count = 0
        max_sub = 0

        for right in range(len(s)):
            if s[right] not in window:
                window.add(s[right])
                count += 1
                max_sub = max(max_sub, count)
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1
                window.add(s[right])
                count = right - left + 1
                max_sub = max(max_sub, count)

        return max_sub
