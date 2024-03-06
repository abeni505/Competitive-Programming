class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x

        while left + 1 < right:
            mid = (left + right)//2

            if mid * mid > x:
                right = mid
            else:
                left = mid

        if x == 1:
            return 1
        return left
