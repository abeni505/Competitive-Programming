class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = [False] * (len(nums) + 1)

        result = 0
        current_flips = False
        for i in range(len(nums) - k + 1):
            current_flips ^= flips[i]
            if nums[i] == current_flips:
                result += 1
                current_flips ^= 1
                flips[i + k] = 1

        for i in range(len(nums) - k + 1, len(nums)):
            current_flips ^= flips[i]
            if nums[i] == current_flips:
                return -1

        return result
   