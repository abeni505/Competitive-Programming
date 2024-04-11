class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1

        drxn = [(1,-1)]

        visited = set()
        queue = deque([("0000",0)])
        visited.add(("0000"))

        def nbr(curr):
            new = []
            for i in range(4):
                for a , b in drxn:
                    newx = (int(curr[i]) + a) % 10
                    newy = (int(curr[i]) + b) % 10

                    new.append(curr[:i] + str(newx) + curr[i + 1:])
                    new.append(curr[:i] + str(newy) + curr[i + 1:])

            return new

    
        while queue:
            
            curr , dist = queue.popleft()

            if curr == target:
                return dist 

          
            for child in nbr(curr):
                if child not in visited and child not in deadends:
                    queue.append((child , dist + 1))
                    visited.add(child)


        return -1


    
                 