"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict(list)
        importance = defaultdict(int)
        for employee in employees:
            u = employee.id
            v = employee.subordinates
            w = employee.importance
        
            importance[u] = w
            graph[u].extend(v)

        total = 0
        
        stack = [id]
        visited = set()
        
        while stack:

            curr = stack.pop()
            if curr in visited:
                continue

            total += importance[curr]
            visited.add(curr)
            for nbr in graph[curr]:
                stack.append(nbr)
        
        return total