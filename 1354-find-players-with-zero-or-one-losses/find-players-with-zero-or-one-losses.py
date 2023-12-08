class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = {win for win,loss in matches}
        lossers = {loss for win,loss in matches}
        count = {}

        for win , loss in matches:
            if win in lossers:
                winners.discard(win)
            count[loss] = 1 + count.get(loss, 0)

        loss_1 = []
        for loss in lossers:
            if count[loss] == 1:
                loss_1.append(loss)
     
        return [sorted(winners),sorted(loss_1)]
