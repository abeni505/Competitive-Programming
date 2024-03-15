class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] *( len(nums) + 1)
        suffix = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] * nums[i]

        for j in range(len(nums) - 1 , -1 , -1):
            suffix[j] = suffix[j + 1] * nums[j]

        prefix = prefix[:len(nums)]
        suffix = suffix[1:]
       

        return [prefix[i] * suffix[i] for i in range(len(nums))]