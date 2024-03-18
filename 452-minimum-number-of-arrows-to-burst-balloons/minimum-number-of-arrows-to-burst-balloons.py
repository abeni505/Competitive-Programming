class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        print(points)
 
        output = [points[0]]

        for i in range(1,len(points)):

            start , end = points[i]

            if start <= output[-1][1]:
                output[-1][1] = min(output[-1][1], end)

            else:
                output.append([start,end])
         
        return len(output)