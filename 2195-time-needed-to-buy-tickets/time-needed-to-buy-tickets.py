class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        count = 0
     
        n = len(tickets)
        for i in range(n):
            
            if i <= k:
                count += min(tickets[k],tickets[i])
            
            else:
                count += min(tickets[k] - 1, tickets[i])

        return count



