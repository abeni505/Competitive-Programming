class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        nums = nums[::-1]
        stack = []
        max_right = float('-inf')

        for i in range(len(nums)):
            if stack and nums[i] < max_right :
                return True
            while stack and stack[-1] < nums[i]:
                max_right = max(max_right, stack.pop()) 
               
            stack.append(nums[i])
        return False

                
