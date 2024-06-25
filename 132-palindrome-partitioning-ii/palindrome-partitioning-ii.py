class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        memo = {}

        def is_palindrome(word):
            return word == word[::-1]

        def dp(i):
            if i == n:
                return -1  

            if i not in memo:
                min_ = float('inf')

                for j in range(i + 1, n + 1):
                    if is_palindrome(s[i:j]):
                        min_ = min(min_, 1 + dp(j))

                memo[i] = min_
            return memo[i]

        return dp(0)

