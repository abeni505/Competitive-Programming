class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        AList = defaultdict(list)


        for parent , child ,cost in flights:
            AList[parent].append((child , cost))

        visited = {}
        heap = [(0,0,src)] # cost , node counted , node

        while heap:
            # print(heap)
            cost, counted , node = heapq.heappop(heap)
            if node == dst:
                return cost
            
            if counted > k or (node in visited and visited[node] <= counted):
                # print(node)
                continue

            visited[node] = counted

            for child , child_cost in AList[node]:
                heapq.heappush(heap , (child_cost + cost ,counted + 1 , child))

        
        # print(AList)
        return -1

