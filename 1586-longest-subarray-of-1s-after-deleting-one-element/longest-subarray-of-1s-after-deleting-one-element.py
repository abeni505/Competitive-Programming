class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = count_0 = 0
        max_ = 0

        for right in range(len(nums)):
            if not nums[right]:
                count_0 += 1
            
            while count_0 > 1:
                if not nums[left]:
                    count_0 -= 1
                left += 1
                       
            max_ = max(max_ , right - left)

        return max_
                

                