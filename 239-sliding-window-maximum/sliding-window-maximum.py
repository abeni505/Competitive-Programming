class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = deque()
        output = []


        for i in range(len(nums)):
            # print(window)
            if window and i - window[0] >= k:
                window.popleft()

            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)
            output.append(nums[window[0]])

        
        return output[k-1:]