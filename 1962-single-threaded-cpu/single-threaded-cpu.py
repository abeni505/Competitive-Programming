class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        

        minheap = []
        
        tasks = sorted((tasks[i][0] , tasks[i][1] , i) for i in range(len(tasks)))

        output = []
        time = 0
        for arrival_time, process_time, indx in tasks:
           
            while minheap and arrival_time > time:
                min_pt , min_indx = heappop(minheap)
                output.append(min_indx)

                time += min_pt

            time = max(time, arrival_time)
            heappush(minheap, (process_time, indx))

        for i in range(len(minheap)):
            output.append(heappop(minheap)[-1])

        return output



        
        
       

