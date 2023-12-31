class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        max_ = float("-inf")

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    max_ = max(max_ , j - i - 1)

        if max_ == float("-inf"):
            return -1
        else:
            return max_                     