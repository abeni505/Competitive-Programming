class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1

        count = pre_right = 0
        for num in nums:
            pre_right += num
            pre_left = pre_right - k

            count += prefix[pre_left]

            prefix[pre_right] += 1

        return count





