class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = set()
        lossers = set()
        
        for win , loss in matches:
            winners.add(win)
            lossers.add(loss)
        
        for win , loss in matches:
            if win in lossers:
                winners.discard(win)

        count = {}
        for win , loss in matches:
            count[loss] = 1 + count.get(loss, 0)

        loss_1 = []
        for loss in lossers:
            if count[loss] == 1:
                loss_1.append(loss)

            
        return [sorted(winners),sorted(loss_1)]
