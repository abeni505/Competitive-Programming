class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def prime_sieve(n):
            isprime = [True] * (n + 1)
            isprime[0] = isprime[1] = False
            
            for i in range(2 , int(sqrt(n)) + 1):
                if isprime[i]:
                    for j in range(i * i , n+1 , i):
                        isprime[j] = False
            return isprime
        
        sieve = prime_sieve(n)
        primes = []
        for i in range(len(sieve)):
            if sieve[i]:
                primes.append(i)

        primes.sort()
        left = 0
        right = len(primes) - 1

        output = []
        while left <= right:
            x ,  y = primes[left] , primes[right]
            if  x + y == n:
                output.append([x, y])
                left += 1
                right -= 1
            elif x + y < n:
                left += 1
            else:
                right -= 1

        return output

