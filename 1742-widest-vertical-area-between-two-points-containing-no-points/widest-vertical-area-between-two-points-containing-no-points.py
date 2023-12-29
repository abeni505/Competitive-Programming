class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        

        points.sort()
        max_ = float('-inf')
        for i in range(len(points) - 1):
            max_ = max(max_, points[i + 1][0] - points[i][0])
        
        return max_