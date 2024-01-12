class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        window = sum(cardPoints[:k])
        max_sum = window

        left = k-1
        right = len(cardPoints) - 1

        for x in range(k):

            window -= cardPoints[left]
            window += cardPoints[right]

            left -= 1
            right -= 1
            
            max_sum = max(max_sum , window)

        return max_sum
        