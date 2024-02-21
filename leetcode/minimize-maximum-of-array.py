class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        
        prefix = list(accumulate(nums))
        max_ = 0
        for i in range(len(prefix)):
            max_ = max(max_ ,ceil(prefix[i]/(i + 1)))
        
        return max_