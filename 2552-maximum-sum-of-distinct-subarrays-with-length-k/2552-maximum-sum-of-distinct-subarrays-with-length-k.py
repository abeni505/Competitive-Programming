class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_max = 0
        curr_sum = 0
        hashset = set()

        for i in range(len(nums)):
            if nums[i] not in hashset:
                if len(hashset) < k:
                    hashset.add(nums[i])
                    curr_sum += nums[i]
                if len(hashset) == k:
                    curr_max = max(curr_max, curr_sum)
                    curr_sum -= nums[i - k + 1]
                    hashset.remove(nums[i - k + 1])
            else:
                hashset = {nums[i - 1], nums[i]}
                curr_sum = sum(hashset)
        return curr_max
