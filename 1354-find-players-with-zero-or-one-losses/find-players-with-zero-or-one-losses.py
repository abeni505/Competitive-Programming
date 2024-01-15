class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winner = defaultdict(int)
        looser = defaultdict(int)

        for x, y in matches:
            winner[x] += 1
            looser[y] += 1
        
        output0 = []
        output1 = []
        for key in winner.keys():
            if key not in looser.keys():
                output0.append(key)
        for key , val in looser.items():
            if val == 1:
                output1.append(key)
        output0.sort()
        output1.sort()
        return [output0 , output1]