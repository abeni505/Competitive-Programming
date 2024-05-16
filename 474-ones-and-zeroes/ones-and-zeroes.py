class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        count = [(i.count("0") , i.count("1")) for i in strs]
        lenn = len(strs)

        memo = {}
        def dp(zero , one , i):
            if (zero , one , i) in memo:
                return memo[(zero , one , i)]

            if zero < 0 or one < 0: 
                return -1
            
            if zero == 0 and one == 0: 
                return 0

            if i == lenn: 
                return 0

            take = 1 + dp(zero - count[i][0], one - count[i][1], i+1)
            not_take = dp(zero , one , i+1)

            memo[(zero, one, i)] = max(take, not_take)

            return memo[(zero, one, i)]

        return dp(m, n, 0)

          