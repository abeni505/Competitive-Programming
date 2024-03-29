class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False

        check = {2 , 3, 5}
        d = 2
        while d * d <= n:
            while n % d == 0:
                n //= d
                if d not in check:
                    return False
            d += 1
        
        if n > 1:
            if n not in check:
                return False
        
        return True
