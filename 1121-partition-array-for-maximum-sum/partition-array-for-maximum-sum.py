class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        memo = defaultdict(int)
        def recur(i):
            if i >= len(arr):
                return 0

            if i in memo:
                return memo[i]
            curr_max = 0
            total_max = 0

            for j in range(i , min(len(arr),i + k)):
                curr_max = max(curr_max , arr[j])
                window = j - i + 1
                total_max = max(total_max , recur(j + 1) + (curr_max * window))

            memo[i] = total_max
            return total_max

        return recur(0)



                
                

            