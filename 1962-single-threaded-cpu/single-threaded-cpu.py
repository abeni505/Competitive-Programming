class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        

        minheap = []
        
        for i in range(len(tasks)):
            arrivaltime , processtime = tasks[i]
            tasks[i] = (arrivaltime,processtime,i)
        tasks.sort()

        output = []
        time = 0
        for arrival_time, process_time, indx in tasks:
    
            while minheap and arrival_time > time:
                next_process_time, next_indx, next_end_time = heappop(minheap)
                output.append(next_indx)
                
                time += next_process_time

            time = max(time, arrival_time)
            end_time = time + process_time
            heappush(minheap, (process_time, indx, end_time))

        for i in range(len(minheap)):
            output.append(heappop(minheap)[1])
       
        return output 





















            # if not minheap:
            #     output.append(i)
            #     heappush(minheap, (processtime , arrivaltime ,endtime, i)
            # else:
                
            #     while minheap:
            #         pt , at , indx, endt = heapopp(minheap)

            #         heappush(minheap, (processtime , arrivaltime , i)

            #         if arrivaltime < endt:
            #             heappush(minheap,pt, at , indx ,endt)

            #         elif arrivaltime >= endtime:
            #             if arrivaltime == endtime:
            #                 a, b , c, d = heappop(minheap)



        
        
       

