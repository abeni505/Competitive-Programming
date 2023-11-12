class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for a in arr1:
            valid = True
            for b in arr2:
                if abs(a - b) <= d:
                    valid = False
                    break

            if valid is True:
                ans += 1

        return ans
