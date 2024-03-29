class Solution:
    def countPrimes(self, n: int) -> int:

        isprime = [1 for _ in range(n + 2)]
        isprime[0] = isprime[1] = 0
        
        d = 2
        while d * d <= n:

            if isprime[d]:
                j = d * d

                while j <= n:
                    isprime[j] = 0
                    j += d
            d += 1

        check = list(accumulate(isprime))
        return check[n - 1]