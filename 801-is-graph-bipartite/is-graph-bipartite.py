class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        


        color = defaultdict(int)
        
        for i in range(len(graph)):

            if i in color:
                continue
            
            stack = [i]
            color[i] = 1

            while stack:
                curr = stack.pop()

                for nbr in graph[curr]:
                    if nbr in color:
                        if color[nbr] == color[curr]:
                            return False
                    else:
                        stack.append(nbr)
                        color[nbr] = 1 - color[curr]
        return True
     

