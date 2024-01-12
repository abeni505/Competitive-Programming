class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        left = cur_max = cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while (nums[right] * (right - left + 1)) - cur_sum > k:
                cur_sum -= nums[left]
                left += 1
                
            cur_max = max(cur_max , right - left + 1)

        return cur_max
