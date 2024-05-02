class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        adjlist = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(n):
            for j in graph[i]:
                adjlist[j].append(i)

            indegree[i] += len(graph[i])
      
        queue = deque([])
        for vertex in range(n):
            if not indegree[vertex]:
                queue.append(vertex)

        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for nbr in adjlist[curr]:
                indegree[nbr] -= 1
                if not indegree[nbr]:
                    queue.append(nbr)

        return sorted(ans)

            
