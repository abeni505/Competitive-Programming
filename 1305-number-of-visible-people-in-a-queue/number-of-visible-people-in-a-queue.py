class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        output = [0]* len(heights)
        stack = []

        for i in range(len(heights)):
            # print(stack)
            while stack and heights[stack[-1]] <= heights[i]:
                output[stack.pop()] += 1

            if stack:
                output[stack[-1]] += 1

            stack.append(i)
        
        return output

