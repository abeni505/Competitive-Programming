class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        check = sorted(score , reverse = True)
   
        output = []
        for i in score:
            if check.index(i) == 0:
                output.append("Gold Medal")
            elif check.index(i) == 1:
                output.append("Silver Medal")
            elif check.index(i) == 2:
                output.append("Bronze Medal")
            else:
                output.append(str(check.index(i) + 1))
        
        return output