class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)

        for x,y,t in meetings:
            graph[x].append((y,t))
            graph[y].append((x,t))

        heap = [(0,firstPerson)] #time,person
        for neighbor,time in graph[0]:
            heapq.heappush(heap,(time,neighbor))
        
        visited = set([0])

        while heap:
            time,person = heapq.heappop(heap)

            if person in visited:
                continue

            visited.add(person)

            for neighbor,neighbor_time in graph[person]:
                if neighbor_time >= time:
                    heapq.heappush(heap,(neighbor_time,neighbor))

        return visited