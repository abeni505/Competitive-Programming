class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        queue = deque()
        deck.sort(reverse = True)

        for i in deck:
            if queue:
                queue.appendleft(queue.pop())

            queue.appendleft(i)

        return queue