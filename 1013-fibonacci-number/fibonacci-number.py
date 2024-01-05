def fibonacci(n):
        if n <= 1:
            return n  
        return  fibonacci(n - 1) + fibonacci(n - 2)
        
class Solution:
    def fib(self, n: int) -> int:
        return  fibonacci(n)

    
