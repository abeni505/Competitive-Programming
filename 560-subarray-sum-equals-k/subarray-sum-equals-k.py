class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = defaultdict(int)
        prefix[0] = 1

        run_sum = count = 0
        for i in nums:
            run_sum += i

            check = run_sum - k
            count += prefix[check]

            prefix[run_sum] += 1
    
        return count

   