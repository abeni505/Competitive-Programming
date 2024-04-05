class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        adjlst = defaultdict(list)

        for u , v in edges:
            adjlst[u].append(v)
            adjlst[v].append(u)

        for key , val in adjlst.items():
            if len(val) == len(edges):
                return key
