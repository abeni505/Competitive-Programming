class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = Counter(nums)

        total = 0
        for val in count.values():
            if val == 1:
                return -1
           
            q = val//3
            r = val % 3
            if r > 0 or q == 0:
                r = 1

            total += q + r

        return total