class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        arr = []
        n = len(nums)
        res = 0

        for left in range(n):
            if nums[left] % 2 == 0 and nums[left] <= threshold:
                arr.append(nums[left])
            else:
                continue

            right = left + 1
            while right < n and arr[-1] % 2 != nums[right] % 2 and nums[right] <= threshold:
                arr.append(nums[right])
                right += 1

            res = max(res, len(arr))
            arr = []

        return res
