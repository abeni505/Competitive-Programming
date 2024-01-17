class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix = [0] * len(nums)
        
        run_sum = 0
        for i in range(len(nums)):
            prefix[i] = (nums[i] + run_sum) % k
            run_sum = prefix[i]
        
        ans = 0
        pre_count = Counter(prefix)
        pre_count[0] += 1

      
        for val in pre_count.values():
            if val > 1:
                ans += val*(val-1)//2

        return ans

        