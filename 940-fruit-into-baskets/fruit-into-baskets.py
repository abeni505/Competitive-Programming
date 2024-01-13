class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = max_len = 0
        window = defaultdict(int)

        for right in range(len(fruits)):
            window[fruits[right]] += 1
            
            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]

                left += 1
                
            max_len = max(max_len , right - left + 1)

        return max_len
        