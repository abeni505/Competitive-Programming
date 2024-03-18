class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x: x[1])
        
        check = points[0][1]

        count = 1
        for start , end in points:
            if start > check:
                count += 1
                check = end

        return count
