class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        stack = []

        trapped = 0
        for i in range(n):
            while stack and height[stack[-1]] <= height[i]:

                top = stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[i]) - height[top]
                    w = i - stack[-1] - 1
                    trapped += h * w

            stack.append(i)

        return trapped