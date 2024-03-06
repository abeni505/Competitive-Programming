class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def helper (target):
            day = 0
            curr = 0
            for i in weights:
                curr += i
                if curr > target:
                    day += 1
                    curr = i

            return day + 1

        left = max(weights) - 1
        right = sum(weights) + 1

        while left + 1 < right:
            mid = (left + right)//2

            if helper(mid) <= days:
                right = mid
            else:
                left = mid

        return right


        