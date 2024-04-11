class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        for u , v in redEdges:
            graph[u].append((v , "R"))
        for u , v in blueEdges:
            graph[u].append((v , "B"))


        queue = deque([(0 , None, 0)])
        visited = set([(0 , None)])

        answer = [-1] * n
        dist = 0
        while queue:

            node , color , dist = queue.popleft()

            if answer[node] == -1:
                answer[node] = dist
            
            for nbr , nbr_color in graph[node]:
                if nbr_color != color and (nbr , nbr_color) not in visited:

                    queue.append((nbr, nbr_color, dist + 1))
                    visited.add((nbr, nbr_color))
                    
            

        return answer

