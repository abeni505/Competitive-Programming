class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        h2 = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != h2[i]:
                count += 1
        
        return count