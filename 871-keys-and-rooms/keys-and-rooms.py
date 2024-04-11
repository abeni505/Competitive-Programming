class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        stack = [0]
        visited = set()
        visited.add(0)

        while stack:
            cur_room = stack.pop()

            for child in rooms[cur_room]:
                if child not in visited:
                    stack.append(child)

                    visited.add(child)
                    
        return len(visited) == len(rooms)