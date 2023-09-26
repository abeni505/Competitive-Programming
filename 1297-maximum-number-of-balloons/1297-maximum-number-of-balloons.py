from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        max = len(text) 
        for i in balloon:
            max = min(max, countText[i] // balloon[i])
        return max
