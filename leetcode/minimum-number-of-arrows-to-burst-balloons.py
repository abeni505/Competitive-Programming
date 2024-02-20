class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points = sorted(points , key = lambda x : x[1])
        check = points[0]
        # print(points)
        count = 1
        for x , y in points:
            if x > check[1]:
                count += 1
                check = [x , y]
                
        return count