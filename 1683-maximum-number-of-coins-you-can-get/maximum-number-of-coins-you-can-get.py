class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort(reverse = True)

        count = 0
        i = 1
        while i < len(piles):

            count += piles[i]
            i += 2
            piles.pop()

        return count
    
