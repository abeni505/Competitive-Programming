def fibonacci(n, hashmap):
        if n <= 1:
            return n  

        if n in hashmap:
            return hashmap[n]

        hashmap[n] = fibonacci(n - 1 , hashmap) + fibonacci(n - 2, hashmap)

        return  hashmap[n]

class Solution:
    def fib(self, n: int) -> int:
        return  fibonacci(n,{})

    
