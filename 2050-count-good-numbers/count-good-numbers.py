class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod =  (10**9 + 7)
        modinverse = 400000003
        def modDivide(a,b,m):
            a = a % m
            inv = modinverse
            return (inv*a) % m

        if n == 1:
            return 5
        if n == 2:
            return 20


        res = self.countGoodNumbers(n//2)
        if (n//2) % 2:
            a = (res*res * 4)
            b = 5
            final = modDivide(a,b,mod)
        else:
            final = (res * res ) % mod

        if n % 2:
            final = (final * 5) % mod
        
        
        
        return final