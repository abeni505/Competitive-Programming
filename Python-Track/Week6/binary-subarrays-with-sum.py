class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        run_sum = count = 0
        for i in nums:
            run_sum += i
            
            check = run_sum - goal
            count += prefix[check]
           
            prefix[run_sum] += 1
    
        return count
