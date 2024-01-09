class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        left = total = 0
        min_len = float('inf') 

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_len = min(min_len , right - left + 1)
                total -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
