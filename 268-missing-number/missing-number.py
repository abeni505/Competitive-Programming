class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        find = 0
        for i in nums:
            find ^= i
        
        for j in range(len(nums) + 1):
            find ^= j
        
        return find
