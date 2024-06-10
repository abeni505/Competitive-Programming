class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        exp = sorted(heights)
        count = 0 
        for i in range(len(heights)):
            if heights[i] != exp[i]:
                count += 1
        
        return count