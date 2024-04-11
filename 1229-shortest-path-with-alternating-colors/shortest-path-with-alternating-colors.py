class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = [[[],[]] for _ in range(n)]

        for a , b in redEdges:
            graph[a][0].append(b)
        
        for a , b in blueEdges:
            graph[a][1].append(b)

      
        RED , BLUE = 0, 1
        queue = deque([(0,RED),(0,BLUE)])
        visited = set([(0,RED),(0,BLUE)])

        answer = [-1] * n
        dist = 0
        while queue:

            for _ in range(len(queue)):
                node , color = queue.popleft()

                if answer[node] == -1:
                    answer[node] = dist

                next_color = 1 - color
                for nbr in graph[node][next_color]:
                    if (nbr , next_color) not in visited:
                        queue.append((nbr , next_color))
                        visited.add((nbr , next_color))
            dist += 1
        
        return answer