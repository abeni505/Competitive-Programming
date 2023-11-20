class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        unique_nums = set()
        for i in nums:
            if i == 0:
                continue
            unique_nums.add(i)
        return len(unique_nums)