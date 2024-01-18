class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        window = deque()
        output = []
        for right in range(len(nums)):
            if window and window[0] <= right - k:
                window.popleft()
            while window and nums[right] > nums[window[-1]]:
                window.pop()

            window.append(right)
            output.append(nums[window[0]])
    

        return output[k-1:]
