class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        
        rooms = [i for i in range(n)]
        minheap = []
        count = [0] * n

        for start , end in meetings:
            
            while minheap and start >= minheap[0][0]:
                curr_end , room = heappop(minheap)
                heappush(rooms,  room)

            if not rooms:
                cur_end , room = heappop(minheap)   
                heappush(rooms , room)

                end = cur_end + (end - start)
            
            room = heappop(rooms)
            count[room] += 1

            heappush(minheap , (end , room))
        
        return count.index(max(count))

