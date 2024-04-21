class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

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
            for nbr in graph[curr]:
                if nbr not in visited:
                    stack.append(nbr)
                    visited.add(nbr)

        return False