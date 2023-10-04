class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins=0

        for i in range((len(piles)//3)):
            piles.pop()
            piles.remove(piles[0])
            coins+=piles[-1]
            piles.pop()

        return coins