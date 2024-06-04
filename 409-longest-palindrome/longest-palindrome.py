class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = Counter(s)
        
        ans = max_odd = 0
        for key , val in count.items():
            if val % 2:
                max_odd = max(max_odd , val)
                ans += val - 1
            else:
                ans += val
                
        if max_odd:
            ans += 1

        return ans

