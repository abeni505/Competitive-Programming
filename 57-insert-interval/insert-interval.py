class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        idx_prev = bisect_left(intervals, newInterval[0], key=lambda x: x[1])  

        idx_nxt = bisect_right(intervals, newInterval[1], key=lambda x: x[0])    

        left = intervals[:idx_prev]
        right = intervals[idx_nxt:]
    
        mid = [newInterval] 
        if idx_nxt > idx_prev:
            mid =[[min(intervals[idx_prev][0], newInterval[0]), max(intervals[idx_nxt - 1][1], newInterval[1])]]


        return left + mid + right