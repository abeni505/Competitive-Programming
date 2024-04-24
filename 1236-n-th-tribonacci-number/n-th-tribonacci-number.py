class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = [0 , 1 , 1]

        if n < 3:
            return memo[n]
        for i in range(3 , n + 1):
            memo[0] , memo[1] , memo[2] = memo[1] , memo[2] , sum(memo)

        return memo[2]