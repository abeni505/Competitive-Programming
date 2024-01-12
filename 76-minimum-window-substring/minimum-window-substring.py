class Solution:
    def minWindow(self, s: str, t: str) -> str:

        check = Counter(t)
        window = defaultdict(int)
        window_d = deque()

        left = 0
        min_len = float('inf') 

        for right in range(len(s)):

            window[s[right]] += 1
            window_d.append(s[right])
            while all(window[key] >= value for key, value in check.items()):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    window_min = deque(window_d)
            
                window[s[left]] -= 1
                window_d.popleft()
                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

        if min_len == float('inf'):
            return ""

        return "".join(window_min)
