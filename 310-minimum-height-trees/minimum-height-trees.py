class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:return [0]

        graph = defaultdict(list)
        degree = defaultdict(int)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        queue = deque([])
        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)

        while n > 2:
            leaves = len(queue)
            n -= leaves

            for _ in range(leaves):
                curr = queue.popleft()

                for nbr in graph[curr]:
                    degree[nbr] -= 1
                    if degree[nbr] == 1:
                        queue.append(nbr)

        return queue




            



