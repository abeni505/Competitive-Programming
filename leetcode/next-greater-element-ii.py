class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        hashmap = {}
        stack = []
        n = len(nums)
        output = [-1] *n
        nums += nums

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                output[stack.pop()%n] = nums[i]

            stack.append(i)

        return output