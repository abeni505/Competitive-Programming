class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        white, gray, black = 0, 1, 2

        graph = defaultdict(list)
        color = defaultdict(int)

        for i in range(len(edges)):
            u = i
            v = edges[i]
            if v != -1:
                graph[u].append(v)
    
        for i in range(len(edges)):
            color[i] = white
        
        cycles = []
        def dfs(node, curr):
            if color[node] == black: 
                return
            
            color[node] = gray
            curr.append(node)
            for nbr in graph[node]:
                if color[nbr] == white:
                    dfs(nbr, curr)
                elif color[nbr] == gray:
                    left = curr.index(nbr)
                    
                    cycles.append(len(curr) - left)
            
            color[node] = black
        
        for i in range(len(edges)):
            if edges[i] != -1:
                dfs(i,[])

        if not cycles:
            return -1
        return max(cycles)



        