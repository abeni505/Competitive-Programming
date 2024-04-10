class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def find_divisors(number):
            divisors = []
            for i in range(1, int(number**0.5) + 1):
                if number % i == 0:
                    divisors.append(i)
                    if i* i != number:
                        divisors.append(number // i)
            return divisors

        factors = find_divisors(n)
        factors.sort()

        return factors[k - 1] if k - 1 < len(factors) else -1