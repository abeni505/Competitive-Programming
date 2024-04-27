class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

      
        visited = set()
        queue = deque([(0, 0, 0)])
        

        while queue:
            indx, correct, lvl = queue.popleft()

            if correct == len(key):  
                return lvl
                
            if (indx, correct) in visited: 
                continue

            visited.add((indx, correct))
            if ring[indx] == key[correct]:
                queue.append((indx, correct + 1, lvl + 1))
            else:
                new_index = (indx + 1) % len(ring) 
                if (new_index , correct) not in visited:
                    queue.append(((indx + 1) % len(ring), correct, lvl + 1))
                
                new_index = (indx - 1) % len(ring) 
                if (new_index , correct) not in visited:
                    queue.append(((indx - 1) % len(ring), correct, lvl + 1))
                