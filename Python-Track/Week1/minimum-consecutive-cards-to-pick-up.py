class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        left = 0
        min_len = float('inf')

        window = defaultdict(int)
        flag = False

        for right in range(len(cards)):
            window[cards[right]] += 1
        
            
            while window[cards[right]] > 1:
                flag = True

                min_len = min(min_len , right - left + 1)
                window[cards[left]] -= 1
                if window[cards[left]] == 0:
                    del window[cards[left]]
                left += 1


        if not flag:
            return -1
        return min_len

            