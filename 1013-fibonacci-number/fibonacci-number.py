class Solution:
    def fib(self, n: int) -> int:

        memo = {}
        if n == 1:return 1
        elif n == 0:return 0

        else:
            ans = self.fib(n - 1) + self.fib(n - 2)
            if ans not in memo:
                memo[n] = ans
            

            return ans
        
    