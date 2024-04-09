class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        

        queue = deque([i for i in range(len(tickets))])

        count = 0
        while queue:
            
            curr = queue.popleft()
            count += 1

            tickets[curr] -= 1

            if tickets[curr]:
                queue.append(curr)
            else:
                if curr == k:
                    break
            

        return count 
