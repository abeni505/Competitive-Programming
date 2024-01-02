class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points.sort(key = lambda x : sqrt(x[0]**2 + x[1]**2))

        output = []
        for i in range(k):
            output.append(points[i])

        return output