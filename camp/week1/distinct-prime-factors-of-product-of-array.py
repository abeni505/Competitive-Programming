class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        n = reduce(lambda x, y : x * y, nums)
       
        primes = set()

        d = 2

        while d*d <= n:
            while n % d == 0:
                primes.add(d)
                n //= d
            
            d += 1
        
        if n > 1:
            primes.add(n)


        return len(primes)