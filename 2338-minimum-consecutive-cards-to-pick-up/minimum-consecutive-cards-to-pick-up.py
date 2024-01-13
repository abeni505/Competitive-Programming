class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        left = 0
        min_ = float('inf')
        window = set()

        for right in range(len(cards)):
            
            while cards[right] in window:

                min_  =  min(min_ , right - left + 1)
                window.discard(cards[left])
                left += 1

            window.add(cards[right])

        return min_ if min_ != float('inf') else -1


