class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(sqrt(c))

        while left <= right:
            target = left**2 + right**2

            if target < c:
                left += 1
            elif target > c:
                right -= 1
            else:
                return True
        
        return False

