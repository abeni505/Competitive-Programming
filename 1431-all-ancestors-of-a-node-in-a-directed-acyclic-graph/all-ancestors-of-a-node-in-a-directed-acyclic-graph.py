class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        reverse_graph = defaultdict(list)
        for u, v in edges:
            reverse_graph[v].append(u)
        
        in_degree = [0] * n
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        

        ancestors = [set() for _ in range(n)]
        
        for node in topo_order:
            for parent in reverse_graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(ancestors[parent])
        
 
        result = [sorted(list(anc)) for anc in ancestors]
        
        return result
        