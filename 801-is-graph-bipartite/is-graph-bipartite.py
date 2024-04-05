class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        


        colors = [-1] * len(graph)
        for i in range(len(graph)):

            if colors[i] == -1:

                stack = [(i , 0)]
                while stack:

                    node , color = stack.pop()

                    if colors[node] == -1:
                        colors[node] = color
                    
                        for nbr in graph[node]:
                            stack.append((nbr , 1 - color))
                    elif colors[node] != color:
                        return False
    
        return True
                        


            
                
        print(colors)

