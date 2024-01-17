class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
       

        prefix = [0] * (n + 1)

        for first , last , seats in bookings:
            prefix[first - 1] += seats
            prefix[last] -= seats
  
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i - 1]
    
        
        return prefix[:-1]
