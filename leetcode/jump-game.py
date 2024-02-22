class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums) - 1
        
        max_i = nums[0] 
        
        for i in range(1,n):

            if i > max_i:
                return False
            else:
                max_i = max(max_i , nums[i] + i)
            
        return max_i >= n
 