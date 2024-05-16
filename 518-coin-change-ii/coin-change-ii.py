class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        memo = {}
        def dp(indx , amount):
            if (indx, amount) in memo:
                return memo[(indx, amount)]
            
            if amount == 0:
                return 1

            if amount < 0 or indx == n:
                return 0
            
            memo[(indx, amount)] = dp(indx,amount - coins[indx]) + dp(indx + 1, amount)
            return memo[(indx, amount)]
    
        return dp(0,amount)