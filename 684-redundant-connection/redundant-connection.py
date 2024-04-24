class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        root = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):

            while x  != root[x]:
                x = root[x]

            return x
        
        output = []
        def union( x , y):

            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    root[rooty] = rootx
                elif rank[rootx] < rank[rootx]:
                    root[rootx] = rooty
                else:
                    root[rootx] = rooty
                    rank[rooty] += 1
            
            else:
                output.extend((x, y))

        for a , b in edges:
            union(a , b)

        return output




