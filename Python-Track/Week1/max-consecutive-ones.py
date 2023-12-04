class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        max_ = 0
        for i in nums:
            if i:
                total += 1
                max_ = max(max_,total)
            else:
                total = 0
        
        return max_