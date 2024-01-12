class Solution:
    def minWindow(self, s: str, t: str) -> str:

        check = Counter(t)
        window = defaultdict(int)

        output = []

        left = 0
        min_len = float('inf') 

        for right in range(len(s)):

            window[s[right]] += 1
            while all(window[key] >= value for key, value in check.items()):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    output = [s[left:right + 1]]
            
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                    
                left += 1

        return output[0] if output else ""
