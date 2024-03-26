class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 1
        check = set(nums)
        while i in check:
            i += 1
            
        return i
       