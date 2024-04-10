class Solution:
    def smallestValue(self, n: int) -> int:
        
        def prime_factors(n):
            primes = []
            d = 2
            while d * d <= n:
                while n % d == 0:
                    primes.append(d)
                    n //= d
                d += 1
            if n > 1:
                primes.append(n)
            return primes

        
        while True:
            curr_sum = sum(prime_factors(n))
            if curr_sum == n:
                return n
            else:
                n = curr_sum

