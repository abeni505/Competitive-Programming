class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque([0])
        visited = set()
        visited.add(0)

        while queue:
            cur_room = queue.popleft()

            for child in rooms[cur_room]:
                if child not in visited:
                    queue.append(child)

                    visited.add(child)

        return len(visited) == len(rooms)