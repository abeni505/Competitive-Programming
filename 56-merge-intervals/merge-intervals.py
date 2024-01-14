class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals , key = lambda x: x[0])

        output = [intervals[0]]

        for x, y in intervals:
            if x <= output[-1][0]:
                output[-1][0] = x
                output[-1][1] = max(output[-1][1], y)
            elif x <= output[-1][1]:
                output[-1][1] = max(output[-1][1], y)
            else:
                output.append([x, y])

        return output
