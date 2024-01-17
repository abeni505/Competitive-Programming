class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1
        
        run_sum = count = 0
        for i in range(len(nums)):
            run_sum = (nums[i] + run_sum) % k

            count += prefix[run_sum]
            prefix[run_sum] += 1

        return count

        