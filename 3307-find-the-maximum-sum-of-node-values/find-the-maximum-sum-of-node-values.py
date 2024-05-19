class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        best_sum = 0
        for n in nums:
            best_sum += max(n, k ^ n)

        cnt = 0
        for n in nums:
            if (k ^ n) > n:
                cnt += 1

        if cnt % 2 != 0:
            min_difference = float('inf')
            for n in nums:
                difference = abs(n - (n ^ k))
                if difference < min_difference:
                    min_difference = difference
            best_sum -= min_difference

        return best_sum
