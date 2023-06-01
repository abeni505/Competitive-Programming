import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr=[]
        indx=[]
        last=[]
        for i in range(len(points)):
            arr.append([math.sqrt(pow(points[i][0],2)+pow(points[i][1],2)),i])
        arr.sort()
        for j in range(k):
            indx.append(arr[j][1])
            last.append(points[indx[j]])
        return last
        
        
           

