class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        distance = []
        for i in range(len(points)):
            for j in range(i + 1 , len(points)):

                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                distance.append((dist , i , j))

        distance.sort()

        root = [i for i in range(len(points))]
        rank = [0] * len(points)
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            
            return x
        
        def union(x , y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_x] = root_y
                    rank[root_y] += 1

        min_distance = 0
        for dist , u , v in distance:
            if find(u) != find(v):
                union(u , v)

                min_distance += dist
            else:
                continue
        
        return min_distance


