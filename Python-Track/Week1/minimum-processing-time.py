class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse = True)

        max_ = 0
        for i in range(3, len(tasks), 4):
            cur_max = tasks[i] + processorTime[i // 4]
            max_ = max(max_, cur_max)

        return max_