class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        hashmap = defaultdict(list)
        for u , v in edges:
            hashmap[u].append(v)
            hashmap[v].append(u)


        visited = set()
        if hashmap[source]:
            stack = [source]
            visited.add(source)

            while stack:
                curr = stack.pop()
                for x in hashmap[curr]:
                    if x not in visited:
                        if x == destination:
                            return True
                        stack.append(x)
                        visited.add(x)
        
        return False
                    

        

                    