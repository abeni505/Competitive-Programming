class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()

        stack = [source]
        visited.add(source)

        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
                
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        
        return False
                    

        

                    