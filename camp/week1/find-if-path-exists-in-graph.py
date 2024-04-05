class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()

        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    if dfs(nbr):
                        return True

            return False   
         
        return dfs(source)
                    

        

                    