class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse = True)

        length = len(tasks)//len(processorTime)

        new_arr = []
        for i in range(length - 1,len(tasks),length):
            new_arr.append(tasks[i])
        
        max_ = 0
        for i in range(len(new_arr)):
            cur_max = new_arr[i] + processorTime[i]
            max_ = max(max_, cur_max)

        return max_