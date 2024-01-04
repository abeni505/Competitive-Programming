class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = Counter(nums)

        total = 0
        for val in count.values():
            if val >= 2:

                q = val//3
                r = val % 3
                if r > 0 or q == 0:
                    r = 1

                total += q + r

            else:
                total = -1
                break


        return total