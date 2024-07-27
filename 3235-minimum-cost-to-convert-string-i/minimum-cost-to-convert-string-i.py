class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def build(original, changed, costs):
            graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
            for ori, ch, cost in zip(original, changed, costs):
                graph[ori][ch] = min(graph[ori][ch], cost)
            return graph
        
        def dijkstra(graph, start_node, target_node):
            if start_node not in graph:
                return float('inf')
            
            visited_nodes = set()
            min_heap = [(0, start_node)]

            while min_heap:
                cost_to_current, current_node = heapq.heappop(min_heap)
                if current_node == target_node:
                    return cost_to_current
                if current_node in visited_nodes:
                    continue
                visited_nodes.add(current_node)
                for neighbor_node in graph[current_node]:
                    if neighbor_node not in visited_nodes:
                        heapq.heappush(min_heap, (cost_to_current + graph[current_node][neighbor_node], neighbor_node))
            return float('inf')
        
        graph = build(original, changed, cost)
        total_cost = 0
        memo = {}

        for s, t in zip(source, target):
            if s != t:
                if (s, t) in memo:
                    cost = memo[(s, t)]
                else:
                    cost = dijkstra(graph, s, t)
                    memo[(s, t)] = cost
                if cost == float('inf'):
                    return -1
                total_cost += cost

        return total_cost
            
            
            
                