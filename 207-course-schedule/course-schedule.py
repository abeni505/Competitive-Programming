class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = defaultdict(list)
        indegree = defaultdict(int)

        for course , pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque([])
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)

        count = 0
        while queue:
            curr = queue.popleft()
            
            count += 1
            for nbr in graph[curr]:
                indegree[nbr] -= 1

                if not indegree[nbr]:
                    queue.append(nbr)

        return count == numCourses


