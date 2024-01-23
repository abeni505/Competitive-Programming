class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        left = count = 0

        cur_prod = 1

        for right in range(len(nums)):
            cur_prod *= nums[right]

            while left <= right and cur_prod >= k:
                cur_prod /= nums[left]
                left += 1

            count += right - left + 1

        return count