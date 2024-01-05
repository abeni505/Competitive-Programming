def fibonacci(n):
        i = 2
        dp = [0 , 1]
        if n == 0:
            return dp[0]
        
        while i <= n:
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp

            i += 1

        return dp[1]

class Solution:
    def fib(self, n: int) -> int:
        return  fibonacci(n)

    
