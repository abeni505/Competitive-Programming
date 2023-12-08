class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums = set(nums)

        set_ = {i for i in range(len(nums)+1)}

        for i in set_:
            if i not in nums:
                return i