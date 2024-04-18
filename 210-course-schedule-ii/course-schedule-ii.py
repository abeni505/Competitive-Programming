class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        color = defaultdict(int)

        for u , v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        white ,gray , black = 1, 2, 3

        output = []

        for i in range(numCourses):
            color[i] = white

        possible = True
        def dfs(node):
            nonlocal possible
            if color[node] == black:
                return 

            if not possible:
                return []

            color[node] = gray
            for nbr in graph[node]:
                if color[nbr] == white:
                    dfs(nbr)
                elif color[nbr] == gray:
                    possible = False
            
            color[node] = black
            output.append(node)

        
        for i in range(numCourses):
            dfs(i)
        
        if possible:
            return output
        else:
            return []
        