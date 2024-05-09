memo = {}
class Solution:
    def fib(self, n: int) -> int:

        if n in memo:
            return memo[n]

        if n < 2:
            return n
      

        ans = self.fib(n - 1) + self.fib(n - 2)
        memo[n] = ans
            

        return memo[n]
        
    