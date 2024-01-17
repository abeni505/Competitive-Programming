class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
       

        prefix = [0] * (n + 1)

        for first , last , seats in bookings:
            prefix[first - 1] += seats
            prefix[last] -= seats
        
        pre_sum = 0
        for i in range(len(prefix)):
            prefix[i] += pre_sum
            pre_sum = prefix[i]

        
        return prefix[:-1]
