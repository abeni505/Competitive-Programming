class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        window = set()

        left = max_sum = cur_sum = 0

        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                cur_sum -= nums[left]
                left += 1

            cur_sum += nums[right]
            window.add(nums[right])

            max_sum = max(max_sum , cur_sum)

        return max_sum
