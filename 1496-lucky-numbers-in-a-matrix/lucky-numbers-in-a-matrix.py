class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        lucky = []
        minn = set()
        for row in matrix:
            minn.add(min(row))

        col = list(zip(*matrix))
     
        for c in col:
            maxx = max(c)
            if maxx in minn:
                lucky.append(maxx)
            
        return lucky



