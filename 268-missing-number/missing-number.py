class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.append(-1)
        
        for i in range(len(nums)):
            while nums[i] != i and nums[i] != -1:
                temp = nums[i]
                    
                nums[i] , nums[temp] = nums[temp] , nums[i]

        return nums.index(-1)