class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        def dp(amount):
            if amount < 0:
                return float('inf')
                
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            minn = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    take = 1 + dp(amount - coin)
                    minn = min(minn, take)

            memo[amount] = minn 
            return memo[amount]

        if dp(amount) == float('inf'):
            return - 1
            
        return dp(amount)