class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        graph = defaultdict(list)
        indegree = defaultdict(int)
        for rich ,  poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1

       
        queue = deque([])
        output = [i for i in range(n)] 
        for vertex in range(n):
            if not indegree[vertex]:
                queue.append(vertex)
      
        while queue:
            curr = queue.popleft()

            for nbr in graph[curr]:
                if quiet[curr] < quiet[nbr]:
                    quiet[nbr] = quiet[curr]

                    output[nbr] = output[curr]
                
                indegree[nbr] -= 1

                if not indegree[nbr]:
                    queue.append(nbr)
        return output



        