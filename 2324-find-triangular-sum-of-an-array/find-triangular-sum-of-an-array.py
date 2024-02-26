class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        
        new = []
        for i in range(1,len(nums)):
            new.append((nums[i - 1] + nums[i]) % 10)


        return self.triangularSum(new)
        


        