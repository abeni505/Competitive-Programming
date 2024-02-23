class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        min_ = [float('inf')]*len(nums)
        stack = []

        for i in range(len(nums)):
            if i != 0:
                if nums[i] > nums[i-1]:
                    min_[i] = nums[i-1]
                if min_[i] > min_[i-1]:
                    min_[i] = min_[i-1]

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack and nums[i] > min_[stack[-1]]:
                return True
                

            stack.append(i)
        
                
        return False