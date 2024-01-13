class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = max_len = 0
        window = defaultdict(int)

        for right in range(len(s)):

            window[s[right]] += 1
            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]


                left += 1
            max_len = max(max_len , right - left + 1)

        return max_len
            