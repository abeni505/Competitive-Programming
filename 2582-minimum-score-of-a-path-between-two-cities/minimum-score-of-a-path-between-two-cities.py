class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        root = list(range(n + 1))
        size = [1] * (n + 1)
        
        roads = sorted(roads , key = lambda x: x[2])

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x

        def union(x , y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    root[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    root[root_x] = root_y
                    size[root_y] += size[root_x]
        total = float('inf')
        for u , v , dist in roads:
            if find(u) != find(v):
                union(u , v)
        
        for u , v , dist in  roads:
            if find(u) == find(v) == find(1):
                total = min(total , dist)    
        
        return total

