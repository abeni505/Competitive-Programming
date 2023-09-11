class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            window = s[i: i + 3]
            if len(window) == 3:
                if len(set(window)) == len(window):
                    count+=1

        return count
