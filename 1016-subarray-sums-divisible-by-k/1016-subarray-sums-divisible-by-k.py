class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        remainder_count = [0] * k
        remainder_count[0] = 1
        count = 0

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum < 0:
                prefix_sum += k
            count += remainder_count[prefix_sum]
            remainder_count[prefix_sum] += 1

        return count
