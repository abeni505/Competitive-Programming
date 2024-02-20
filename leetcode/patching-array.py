class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        unreach = 1
        patch = 0
        i = 0
        while unreach <= n:
            if i < len(nums) and unreach >= nums[i]:
               
                unreach += nums[i]
                i += 1
            else:
                patch += 1
                unreach *= 2

        return patch